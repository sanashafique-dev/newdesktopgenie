
import streamlit as st
import streamlit.components.v1 as components
import html

# =========================================================
# IMPORTS
# =========================================================

from voice.speech_to_text import speech_to_text
from voice.text_to_speech import speak

from automation.apps import open_application
from automation.browser import google_search, open_website
from automation.whatsapp import handle_whatsapp_command

from automation.files import (
    create_file,
    create_folder,
    rename_file,
    delete_file,
    open_file,
    open_folder,
    list_files,
    move_file,
    copy_file,
    find_file,
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DesktopGenie",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================================
       MAIN APP
       ============================================== */

    .stApp {
        background: #0b0d10;
        color: #ffffff;
    }

    .main .block-container {
        max-width: 1100px;
        padding-top: 1rem;
        padding-bottom: 120px;
    }

    /* ==============================================
       SIDEBAR
       ============================================== */

    section[data-testid="stSidebar"] {
        background: #111318;
        border-right: 1px solid #24272e;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    .sidebar-logo {
        text-align: center;
        font-size: 34px;
        margin-bottom: 5px;
    }

    .sidebar-title {
        text-align: center;
        font-size: 21px;
        font-weight: 700;
        color: white;
    }

    .sidebar-subtitle {
        text-align: center;
        color: #777d88;
        font-size: 12px;
        margin-bottom: 25px;
    }

    /* ==============================================
       BUTTONS
       ============================================== */

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #2a2d34;
        background: #17191f;
        color: #ffffff;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #555b68;
        background: #20232a;
    }

    /* ==============================================
       CHAT INPUT
       ============================================== */

    div[data-testid="stChatInput"] {
        position: fixed;
        bottom: 18px;
        left: 50%;
        transform: translateX(-50%);
        width: min(850px, 90%);
        z-index: 999;
    }

    div[data-testid="stChatInput"] textarea {
        background: #17191f !important;
        color: white !important;
        border: 1px solid #343840 !important;
        border-radius: 15px !important;
    }

    /* ==============================================
       CHAT MESSAGES
       ============================================== */

    div[data-testid="stChatMessage"] {
        border-radius: 14px;
        margin-bottom: 10px;
    }

    /* ==============================================
       FEATURE CARDS
       ============================================== */

    div[data-testid="stAlert"] {
        border-radius: 14px;
        border: 1px solid #282c33;
    }

    /* ==============================================
       SCROLLBAR
       ============================================== */

    ::-webkit-scrollbar {
        width: 7px;
    }

    ::-webkit-scrollbar-track {
        background: #0b0d10;
    }

    ::-webkit-scrollbar-thumb {
        background: #30343c;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "recent_chats" not in st.session_state:
    st.session_state.recent_chats = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">🤖</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-title">DesktopGenie</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'AI Desktop Automation Assistant'
        '</div>',
        unsafe_allow_html=True,
    )

    if st.button("＋  New Chat", use_container_width=True):

        if st.session_state.messages:

            first_message = st.session_state.messages[0]["content"]

            if first_message not in st.session_state.recent_chats:
                st.session_state.recent_chats.insert(
                    0,
                    first_message
                )

            st.session_state.recent_chats = (
                st.session_state.recent_chats[:5]
            )

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.markdown("### Recent Chats")

    if st.session_state.recent_chats:

        for chat in st.session_state.recent_chats:

            short_chat = chat[:35]

            if len(chat) > 35:
                short_chat += "..."

            st.caption("💬 " + short_chat)

    else:

        st.caption("No recent chats")

    st.markdown("---")

    st.markdown("### ⚙️ Settings")

    st.caption("DesktopGenie")
    st.caption("AI Desktop Automation")
    st.caption("Voice Enabled 🎤")
    st.caption("WhatsApp Enabled 💬")


# =========================================================
# COMMAND EXECUTOR
# =========================================================

def execute_command(command):

    command = command.strip()

    if not command:
        return "⚠️ Please enter a command."

    command_lower = command.lower()

    # =====================================================
    # WHATSAPP
    # =====================================================

    whatsapp_keywords = [
        "open whatsapp",
        "launch whatsapp",
        "message ",
        "msg ",
        "send whatsapp message",
    ]

    if any(
        keyword in command_lower
        for keyword in whatsapp_keywords
    ):

        result = handle_whatsapp_command(command)

        return result

    # =====================================================
    # GOOGLE SEARCH
    # =====================================================

    if command_lower.startswith("search google for "):

        query = command[len("search google for "):].strip()

        if not query:
            return "⚠️ Please tell me what you want to search."

        return google_search(query)

    if command_lower.startswith("google search "):

        query = command[len("google search "):].strip()

        if not query:
            return "⚠️ Please tell me what you want to search."

        return google_search(query)

    # =====================================================
    # WEBSITE
    # =====================================================

    if command_lower.startswith("open website "):

        site = command[len("open website "):].strip().lower()

        return open_website(site)

    # =====================================================
    # OPEN APPLICATIONS
    # =====================================================

    app_commands = [
        "open chrome",
        "open google chrome",
        "open calculator",
        "open notepad",
        "open explorer",
        "open file explorer",
        "open task manager",
        "open command prompt",
        "open cmd",
    ]

    if command_lower in app_commands:

        result = open_application(command)

        return result

    # =====================================================
    # FILE MANAGEMENT
    # =====================================================

    # CREATE FILE

    if command_lower.startswith("create file "):

        filename = command[len("create file "):].strip()

        if not filename:
            return "⚠️ Please provide a file name."

        return create_file(filename)

    # CREATE FOLDER

    if command_lower.startswith("create folder "):

        foldername = command[len("create folder "):].strip()

        if not foldername:
            return "⚠️ Please provide a folder name."

        return create_folder(foldername)

    # RENAME FILE

    if command_lower.startswith("rename file "):

        content = command[len("rename file "):].strip()

        parts = content.split(" to ")

        if len(parts) != 2:
            return "⚠️ Format: rename file oldname to newname"

        old_name = parts[0].strip()
        new_name = parts[1].strip()

        return rename_file(old_name, new_name)

    # DELETE FILE

    if command_lower.startswith("delete file "):

        filename = command[len("delete file "):].strip()

        if not filename:
            return "⚠️ Please provide a file name."

        return delete_file(filename)

    # OPEN FILE

    if command_lower.startswith("open file "):

        filename = command[len("open file "):].strip()

        if not filename:
            return "⚠️ Please provide a file name."

        return open_file(filename)

    # OPEN FOLDER

    if command_lower.startswith("open folder "):

        foldername = command[len("open folder "):].strip()

        if not foldername:
            return "⚠️ Please provide a folder name."

        return open_folder(foldername)

    # LIST FILES

    if command_lower in [
        "list files",
        "show files",
        "list my files",
    ]:

        return list_files()

    # FIND FILE

    if command_lower.startswith("find file "):

        filename = command[len("find file "):].strip()

        if not filename:
            return "⚠️ Please provide a file name."

        return find_file(filename)

    # MOVE FILE

    if command_lower.startswith("move file "):

        content = command[len("move file "):].strip()

        parts = content.split(" to ")

        if len(parts) != 2:
            return "⚠️ Format: move file filename to folder"

        source = parts[0].strip()
        destination = parts[1].strip()

        return move_file(source, destination)

    # COPY FILE

    if command_lower.startswith("copy file "):

        content = command[len("copy file "):].strip()

        parts = content.split(" to ")

        if len(parts) != 2:
            return "⚠️ Format: copy file filename to folder"

        source = parts[0].strip()
        destination = parts[1].strip()

        return copy_file(source, destination)

    # =====================================================
    # HELP
    # =====================================================

    if command_lower in [
        "help",
        "what can you do",
        "commands",
    ]:

        return (
            "🤖 **DesktopGenie can help you with:**\n\n"
            "🌐 Open Chrome, Calculator, Notepad, Explorer\n\n"
            "🔎 Search Google\n\n"
            "📁 Create, open, rename, delete and find files\n\n"
            "📂 Create and open folders\n\n"
            "💬 Send WhatsApp messages\n\n"
            "🎤 Use voice commands"
        )

    # =====================================================
    # DEFAULT
    # =====================================================

    return (
        "🤔 I couldn't understand that command.\n\n"
        "Try something like:\n"
        "• Open Chrome\n"
        "• Open Calculator\n"
        "• Search Google for Python\n"
        "• Create file test.txt\n"
        "• List files\n"
        "• Open WhatsApp\n"
        "• Message Sana Kaisi ho"
    )


# =========================================================
# HERO SECTION
# =========================================================

if not st.session_state.messages:

    components.html(
        """
        <!DOCTYPE html>

        <html>

        <head>

        <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            background: transparent;
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;
            color: white;
        }

        .hero {
            height: 270px;

            display: flex;
            flex-direction: column;

            justify-content: center;
            align-items: center;

            text-align: center;
        }

        .robot {
            font-size: 58px;

            margin-bottom: 10px;

            animation:
                floatRobot 3s ease-in-out infinite;
        }

        .title {
            font-size: 48px;
            font-weight: 750;

            letter-spacing: -1.5px;

            margin-bottom: 10px;

            animation:
                glowTitle 3s ease-in-out infinite;
        }

        .title span {
            display: inline-block;

            animation:
                letterWave 2.5s ease-in-out infinite;
        }

        .title span:nth-child(1) {
            animation-delay: 0s;
        }

        .title span:nth-child(2) {
            animation-delay: 0.08s;
        }

        .title span:nth-child(3) {
            animation-delay: 0.16s;
        }

        .title span:nth-child(4) {
            animation-delay: 0.24s;
        }

        .title span:nth-child(5) {
            animation-delay: 0.32s;
        }

        .title span:nth-child(6) {
            animation-delay: 0.40s;
        }

        .title span:nth-child(7) {
            animation-delay: 0.48s;
        }

        .title span:nth-child(8) {
            animation-delay: 0.56s;
        }

        .title span:nth-child(9) {
            animation-delay: 0.64s;
        }

        .title span:nth-child(10) {
            animation-delay: 0.72s;
        }

        .title span:nth-child(11) {
            animation-delay: 0.80s;
        }

        .title span:nth-child(12) {
            animation-delay: 0.88s;
        }

        .subtitle {
            color: #969aa7;

            font-size: 16px;

            margin-bottom: 18px;
        }

        .status {
            color: #aeb2bd;

            font-size: 13px;
        }

        .dot {
            color: #4ade80;

            animation:
                pulse 1.6s ease-in-out infinite;
        }

        @keyframes floatRobot {

            0%, 100% {
                transform: translateY(0px);
            }

            50% {
                transform: translateY(-10px);
            }

        }

        @keyframes glowTitle {

            0%, 100% {
                opacity: 1;
            }

            50% {
                opacity: 0.82;
            }

        }

        @keyframes letterWave {

            0%, 70%, 100% {
                transform: translateY(0px);
            }

            35% {
                transform: translateY(-5px);
            }

        }

        @keyframes pulse {

            0%, 100% {
                opacity: 1;
            }

            50% {
                opacity: 0.3;
            }

        }

        </style>

        </head>

        <body>

        <div class="hero">

            <div class="robot">
                🤖
            </div>

            <div class="title">

                <span>D</span>
                <span>e</span>
                <span>s</span>
                <span>k</span>
                <span>t</span>
                <span>o</span>
                <span>p</span>
                <span>G</span>
                <span>e</span>
                <span>n</span>
                <span>i</span>
                <span>e</span>

            </div>

            <div class="subtitle">
                Your AI-powered desktop automation assistant
            </div>

            <div class="status">

                <span class="dot">●</span>

                Ready to automate your desktop

            </div>

        </div>

        </body>

        </html>
        """,
        height=300,
        scrolling=False,
    )

    st.write("")

    # =====================================================
    # FEATURE CARDS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "**🌐 Open Applications**\n\n"
            'Try: "Open Chrome" or "Open Calculator"'
        )

        st.info(
            "**📁 Manage Files**\n\n"
            "Create, open, rename, delete or find files"
        )

    with col2:

        st.info(
            "**🔎 Web Search**\n\n"
            'Try: "Search Google for Python tutorials"'
        )

        st.info(
            "**💬 WhatsApp**\n\n"
            'Try: "Message Sana Kaisi ho"'
        )


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    role = message["role"]

    content = message["content"]

    with st.chat_message(role):

        st.markdown(content)


# =========================================================
# VOICE BUTTON
# =========================================================

voice_col1, voice_col2 = st.columns([8, 1])

with voice_col2:

    voice_clicked = st.button(
        "🎤",
        help="Speak to DesktopGenie",
    )


# =========================================================
# VOICE PROCESSING
# =========================================================

if voice_clicked:

    with st.spinner("🎤 Listening..."):

        voice_text = speech_to_text()

    if voice_text:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": voice_text,
            }
        )

        with st.spinner("🤖 DesktopGenie is working..."):

            result = execute_command(voice_text)

        if result is None:
            result = "✅ Done."

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": str(result),
            }
        )

        try:
            speak(str(result))
        except Exception:
            pass

        st.rerun()

    else:

        st.warning(
            "🎤 I couldn't hear you. Please try again."
        )


# =========================================================
# CHAT INPUT
# =========================================================

prompt = st.chat_input(
    "Message DesktopGenie..."
)


# =========================================================
# TEXT PROCESSING
# =========================================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.spinner("🤖 DesktopGenie is working..."):

        result = execute_command(prompt)

    if result is None:
        result = "✅ Done."

    result = str(result)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result,
        }
    )

    # Speak response

    try:
        speak(result)
    except Exception:
        pass

    st.rerun()
