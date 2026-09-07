
"""
whatsapp.py - WhatsApp Desktop Automation

Supported commands:

    open whatsapp
    open whatsapp desktop
    launch whatsapp

    message Sana Kaisi ho
    msg Sana Kaisi ho

    send whatsapp message to Sana Kaisi ho

    open whatsapp and message Sana Kaisi ho
    open whatsapp and msg Sana Kaisi ho
"""

import subprocess
import time

import pyautogui
import pygetwindow as gw


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3


# =========================================================
# OPEN WHATSAPP
# =========================================================

def open_whatsapp():
    try:
        subprocess.Popen("start whatsapp:", shell=True)

        time.sleep(4)

        focus_whatsapp_window()

        return True

    except Exception as e:
        print(f"WhatsApp open nahi hua: {e}")
        return False


# =========================================================
# GET WHATSAPP WINDOW
# =========================================================

def get_whatsapp_window():
    try:
        windows = gw.getWindowsWithTitle("WhatsApp")

        if not windows:
            return None

        return windows[0]

    except Exception as e:
        print(f"WhatsApp window nahi mili: {e}")
        return None


# =========================================================
# FOCUS WHATSAPP WINDOW
# =========================================================

def focus_whatsapp_window():
    try:
        win = get_whatsapp_window()

        if not win:
            return False

        if win.isMinimized:
            win.restore()
            time.sleep(0.5)

        win.activate()
        time.sleep(0.8)

        return True

    except Exception as e:
        print(f"Window focus nahi hui: {e}")
        return False


# =========================================================
# SEARCH CONTACT
# =========================================================

def search_contact(name):
    if not focus_whatsapp_window():
        return False

    try:
        pyautogui.hotkey("ctrl", "f")
        time.sleep(0.7)

        pyautogui.write(name, interval=0.05)

        time.sleep(2)

        pyautogui.press("enter")

        time.sleep(2)

        focus_whatsapp_window()
        time.sleep(0.5)

        return True

    except Exception as e:
        print(f"Contact search error: {e}")
        return False


# =========================================================
# CLICK MESSAGE BOX
# =========================================================

def click_message_box():
    try:
        win = get_whatsapp_window()

        if not win:
            return False

        left = win.left
        top = win.top
        width = win.width
        height = win.height

        if width <= 0 or height <= 0:
            return False

        # WhatsApp message box:
        # right side + bottom area
        click_x = int(left + (width * 0.75))
        click_y = int(top + (height * 0.91))

        pyautogui.click(click_x, click_y)

        time.sleep(0.8)

        return True

    except Exception as e:
        print(f"Message box click error: {e}")
        return False


# =========================================================
# TYPE AND SEND MESSAGE
# =========================================================

def type_and_send_message(message):
    try:
        if not focus_whatsapp_window():
            return False

        time.sleep(0.5)

        if not click_message_box():
            return False

        time.sleep(0.5)

        pyautogui.write(
            message,
            interval=0.03
        )

        time.sleep(0.8)

        pyautogui.press("enter")

        time.sleep(1)

        return True

    except Exception as e:
        print(f"Message typing error: {e}")
        return False


# =========================================================
# SEND MESSAGE
# =========================================================

def send_message(name, message):
    success = open_whatsapp()

    if not success:
        return "❌ WhatsApp open nahi ho saka."

    time.sleep(1)

    contact_found = search_contact(name)

    if not contact_found:
        return f"❌ WhatsApp contact '{name}' search nahi ho saka."

    time.sleep(1)

    sent = type_and_send_message(message)

    if not sent:
        return "❌ Message box mein message type ya send nahi ho saka."

    return f"✅ '{name}' ko message bhej diya: {message}"


# =========================================================
# PARSE MESSAGE CONTENT
# =========================================================

def parse_message_content(content):
    content = content.strip()

    if " " not in content:
        return None, None

    name, message = content.split(" ", 1)

    name = name.strip()
    message = message.strip()

    if not name or not message:
        return None, None

    return name, message


# =========================================================
# HANDLE WHATSAPP COMMAND
# =========================================================

def handle_whatsapp_command(command):

    command = command.strip()
    command_lower = command.lower()

    # -----------------------------------------------------
    # OPEN WHATSAPP + MSG
    # -----------------------------------------------------

    combined_prefixes = [
        "open whatsapp and message ",
        "open whatsapp and msg ",
    ]

    for prefix in combined_prefixes:

        if command_lower.startswith(prefix):

            content = command[len(prefix):].strip()

            name, message = parse_message_content(content)

            if not name or not message:
                return (
                    "⚠️ Format: "
                    "open whatsapp and msg <name> <text>"
                )

            success = open_whatsapp()

            if not success:
                return "❌ WhatsApp open nahi ho saka."

            time.sleep(1)

            contact_found = search_contact(name)

            if not contact_found:
                return (
                    f"❌ WhatsApp contact "
                    f"'{name}' search nahi ho saka."
                )

            time.sleep(1)

            sent = type_and_send_message(message)

            if not sent:
                return (
                    "❌ Message box mein message "
                    "type ya send nahi ho saka."
                )

            return (
                f"✅ WhatsApp khol kar "
                f"'{name}' ko message bhej diya: "
                f"{message}"
            )

    # -----------------------------------------------------
    # OPEN WHATSAPP ONLY
    # -----------------------------------------------------

    if command_lower in [
        "open whatsapp",
        "open whatsapp desktop",
        "launch whatsapp",
    ]:

        success = open_whatsapp()

        if success:
            return "✅ WhatsApp khol diya."

        return "❌ WhatsApp open nahi ho saka."

    # -----------------------------------------------------
    # MESSAGE COMMAND
    # -----------------------------------------------------

    if command_lower.startswith("message "):

        content = command[len("message "):].strip()

        name, message = parse_message_content(content)

        if not name or not message:
            return "⚠️ Format: message <name> <text>"

        return send_message(name, message)

    # -----------------------------------------------------
    # MSG COMMAND
    # -----------------------------------------------------

    if command_lower.startswith("msg "):

        content = command[len("msg "):].strip()

        name, message = parse_message_content(content)

        if not name or not message:
            return "⚠️ Format: msg <name> <text>"

        return send_message(name, message)

    # -----------------------------------------------------
    # SEND WHATSAPP MESSAGE TO
    # -----------------------------------------------------

    prefix = "send whatsapp message to "

    if command_lower.startswith(prefix):

        content = command[len(prefix):].strip()

        name, message = parse_message_content(content)

        if not name or not message:
            return (
                "⚠️ Format: "
                "send whatsapp message to <name> <text>"
            )

        return send_message(name, message)

    # -----------------------------------------------------
    # UNKNOWN COMMAND
    # -----------------------------------------------------

    return (
        "⚠️ WhatsApp command samajh nahi aaya.\n\n"
        "Try:\n"
        "• Open WhatsApp\n"
        "• Message Sana Kaisi ho\n"
        "• Msg Sana Kaisi ho\n"
        "• Open WhatsApp and msg Sana Kaisi ho"
    )


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    result = handle_whatsapp_command(
        "open whatsapp and msg Sana Kaisi ho"
    )

    print(result)
