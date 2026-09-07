
import os
import ollama
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3:latest"
)

# Ollama local client
client = ollama.Client(
    host=OLLAMA_BASE_URL
)


def ask_ollama(prompt):
    """
    Send a normal conversation prompt to the local Ollama model.
    """

    try:
        response = client.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"⚠️ Ollama error: {e}"


def is_automation_command(command):
    """
    Check whether the user command should be handled
    by DesktopGenie's automation system.
    """

    command = command.lower().strip()

    automation_prefixes = (
        "open ",
        "launch ",
        "start ",
        "create file ",
        "create folder ",
        "delete file ",
        "rename file ",
        "move file ",
        "copy file ",
        "find file ",
        "find ",
        "list files",
        "show files",
        "show desktop",
        "google ",
        "search google for ",
        "open whatsapp",
        "launch whatsapp",
        "message ",
        "msg ",
        "send whatsapp message to ",
    )

    return command.startswith(automation_prefixes)


def process_command(command, automation_function=None):
    """
    Main AI command processor.

    Automation commands are sent to the existing
    DesktopGenie automation router.

    Normal conversation is handled by Ollama.
    """

    command = command.strip()

    if not command:
        return "Please tell me what you would like me to do."

    # -------------------------------------------------
    # AUTOMATION
    # -------------------------------------------------

    if is_automation_command(command):

        if automation_function is not None:
            try:
                return automation_function(command)
            except Exception as e:
                return f"⚠️ Automation error: {e}"

    # -------------------------------------------------
    # NORMAL AI CHAT
    # -------------------------------------------------

    system_prompt = """
You are DesktopGenie, a friendly AI-powered desktop assistant.

You can have normal conversations with the user.
Answer greetings, questions, explanations and casual conversation naturally.

Important:
Do not pretend that you performed a desktop action unless the
DesktopGenie automation system actually performed it.

Keep responses helpful and reasonably concise.
"""

    try:

        response = client.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"⚠️ Ollama error: {e}"
