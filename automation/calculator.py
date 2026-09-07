import ctypes
import math
import re
import subprocess
import time
from ctypes import wintypes

import pyautogui
import pygetwindow as gw

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

user32 = ctypes.windll.user32

is_open = False

NUMPAD_KEY = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
}

ONES = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
}
TEENS = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19,
}
TENS = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
}
SCALE = {"hundred": 100, "thousand": 1000}

OPERATOR_WORDS = [
    ("multiplied by", "*"),
    ("divided by", "/"),
    ("square root of", "@"),
    ("square root", "@"),
    ("percent of", "%"),
    ("percentage", "%"),
    ("take away", "-"),
    ("subtract", "-"),
    ("minus", "-"),
    ("multiply", "*"),
    ("divided", "/"),
    ("divide", "/"),
    ("plus", "+"),
    ("product", "*"),
    ("times", "*"),
    ("sum of", "+"),
    ("sum", "+"),
    ("add", "+"),
    ("is equal to", "="),
    ("equal to", "="),
    ("equals", "="),
    ("equal", "="),
    ("point", "."),
    ("decimal", "."),
    ("dot", "."),
]


def _single_value(word):
    if word in ONES:
        return ONES[word]
    if word in TEENS:
        return TEENS[word]
    if word in TENS:
        return TENS[word]
    return None


def _consume_number(tokens, i):
    total = 0
    chunk = 0
    j = i
    matched = False
    while j < len(tokens):
        word = tokens[j]
        value = _single_value(word)
        if value is None:
            break
        matched = True
        if value >= 20:
            if chunk:
                total += chunk
            chunk = value
        else:
            chunk += value
        j += 1
        if j < len(tokens) and tokens[j] in SCALE:
            total += (chunk or 1) * SCALE[tokens[j]]
            chunk = 0
            j += 1
    if not matched:
        return None, i
    total += chunk
    return total, j


def text_to_expression(text):
    t = text.lower().strip()
    for word, symbol in OPERATOR_WORDS:
        t = re.sub(r"\b" + re.escape(word) + r"\b", f" {symbol} ", t)
    tokens = t.split()
    out = []
    i = 0
    while i < len(tokens):
        num, j = _consume_number(tokens, i)
        if num is not None:
            out.append(str(num))
            i = j
        else:
            out.append(tokens[i])
            i += 1
    return "".join(out)


def expression_to_keys(expr):
    keys = []
    for ch in expr:
        if ch.isdigit():
            keys.append(("num" + ch).replace("num0", "num0"))
        elif ch == ".":
            keys.append("decimal")
        elif ch in NUMPAD_KEY:
            keys.append(NUMPAD_KEY[ch])
        elif ch in ("%", "+-*"):
            keys.append(("key", ch))
        elif ch == "=":
            keys.append("enter")
        else:
            continue
    return keys


def type_expression(expr):
    for key in expression_to_keys(expr):
        if isinstance(key, tuple) and key[0] == "key":
            pyautogui.write(key[1])
        else:
            pyautogui.press(key)


def _find_calc_hwnds():
    results = []

    @ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def _enum_callback(hwnd, lparam):
        length = user32.GetWindowTextLengthW(hwnd)
        buf = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buf, length + 1)
        if "calculator" in buf.value.lower():
            results.append(hwnd)
        return True

    user32.EnumWindows(_enum_callback, 0)
    return results


def _focus_window():
    try:
        hwnds = _find_calc_hwnds()
        if hwnds:
            hwnd = hwnds[0]
            user32.ShowWindow(hwnd, 9)  # SW_RESTORE
            user32.SetForegroundWindow(hwnd)
            time.sleep(0.4)
            user32.SetForegroundWindow(hwnd)
            time.sleep(0.4)
            return True
    except Exception:
        pass
    try:
        windows = gw.getWindowsWithTitle("Calculator")
        if windows:
            win = windows[0]
            if win.isMinimized:
                win.restore()
            win.activate()
            time.sleep(0.4)
            return True
    except Exception:
        pass
    return False


def evaluate(expr):
    e = expr.strip().rstrip("=")
    e = re.sub(r"@\s*([\d.]+)", r"sqrt(\1)", e)
    e = e.replace("%", "/100")
    if not re.fullmatch(r"[\d+\-*/().\sA-Za-z]+", e):
        return None
    try:
        result = eval(e, {"__builtins__": {}}, {"sqrt": math.sqrt, "abs": abs})
        return int(result) if isinstance(result, float) and result.is_integer() else result
    except Exception:
        return None


def open_calculator():
    global is_open
    subprocess.Popen("start calc", shell=True)
    time.sleep(2.5)
    _focus_window()
    is_open = True
    return "Calculator khol diya. Ab calculation batao."


def calculate(text):
    global is_open
    if not is_open:
        open_calculator()
    expr = text_to_expression(text)
    if not expr:
        return "Koi calculation samajh nahi aayi."
    _focus_window()
    time.sleep(0.5)
    type_expression(expr)
    pyautogui.press("enter")
    result = evaluate(expr)
    answer = f" = {result}" if result is not None else ""
    return f"Calculator mein type kiya: {expr}{answer}"


if __name__ == "__main__":
    test_cases = [
        "five plus three",
        "twenty five times four",
        "one hundred minus twenty",
        "100 + 50",
        "ten divided by two",
        "six point five plus one",
    ]
    for case in test_cases:
        print(f"{case!r:35} -> {text_to_expression(case)}")