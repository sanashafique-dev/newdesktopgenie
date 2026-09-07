# 🤖 DesktopGenie

### AI-Powered Desktop Automation Assistant

> **Talk to your computer. Let DesktopGenie do the work.**

DesktopGenie is an AI-powered desktop automation assistant designed to make everyday computer tasks faster, easier, and more interactive.

It combines a **ChatGPT-style interface, voice commands, speech recognition, text-to-speech, desktop automation, file management, web search, and WhatsApp automation** into a single intelligent assistant.

Instead of manually navigating through multiple applications, users can simply tell DesktopGenie what they want to do.

---

## ✨ Why DesktopGenie?

Modern computer users repeatedly perform simple tasks such as:

* Opening applications
* Searching the web
* Managing files and folders
* Sending messages
* Navigating between applications
* Performing repetitive desktop actions

DesktopGenie aims to turn these manual tasks into simple **natural-language commands**.

### Example

Instead of:

> Open Chrome → Go to Google → Search for Python tutorials

The user can simply say:

> **"Search Google for Python tutorials."**

DesktopGenie understands the command and performs the required action.

---

# 🚀 Key Features

## 🎙️ Voice Control

Control your computer using your voice.

DesktopGenie uses speech recognition to convert spoken commands into text and then executes the requested task.

**Example:**

> "Open Chrome"

> "Open Calculator"

---

## 💬 ChatGPT-Style Interface

DesktopGenie provides a modern conversational interface with:

* Dark theme
* Sidebar navigation
* New Chat option
* Chat history
* Text input
* Voice input
* Assistant responses
* Interactive feature cards

The interface is designed to provide a familiar and intuitive AI assistant experience.

---

## 🖥️ Application Automation

DesktopGenie can launch commonly used Windows applications.

### Supported applications include:

* Google Chrome
* Notepad
* Calculator
* File Explorer
* Task Manager
* Command Prompt

**Example commands:**

```text
Open Chrome
Open Calculator
Open Notepad
Open Explorer
Open Task Manager
Open Command Prompt
```

---

# 📁 File Management

DesktopGenie can perform common file and folder operations.

### Supported operations:

* Create files
* Create folders
* Rename files
* Delete files
* Open files
* Open folders
* List files
* Find files
* Move files
* Copy files

**Example commands:**

```text
Create a file named notes.txt
Create a folder named Projects
Rename notes.txt to ideas.txt
Find my project files
Open the Projects folder
```

---

# 🌐 Web Automation

DesktopGenie can interact with the web browser to perform basic web-related tasks.

### Supported features:

* Google Search
* Open websites
* Open YouTube
* Open Gmail
* Open GitHub
* Open WhatsApp Web

**Example:**

```text
Search Google for machine learning tutorials
Open YouTube
Open GitHub
Open Gmail
```

---

# 📱 WhatsApp Automation

DesktopGenie can automate WhatsApp Desktop for messaging.

Users can open WhatsApp and send a message through a simple command.

### Example:

```text
Open WhatsApp
```

```text
Message Sana Kaisi ho
```

```text
Open WhatsApp and msg Sana Kaisi ho
```

DesktopGenie automatically:

1. Opens WhatsApp
2. Searches for the contact
3. Opens the conversation
4. Types the message
5. Sends the message

---

# 🔊 Text-to-Speech

DesktopGenie can respond using voice.

The assistant converts its response into natural speech using **Microsoft Edge TTS**.

This makes the interaction more natural and allows DesktopGenie to behave like a real desktop assistant.

---

# 🧠 AI Command Processing

DesktopGenie's architecture is designed around the idea of separating **understanding** from **execution**.

The system can identify the user's intent and route the command to the appropriate automation module.

### Conceptual architecture:

```text
              👤 USER
                 │
        ┌────────┴────────┐
        │                 │
     🎙️ Voice          💬 Chat
        │                 │
        ▼                 ▼
 Speech-to-Text       User Input
        │                 │
        └────────┬────────┘
                 ▼
        🧠 Command Processing
                 │
        ┌────────┼─────────┐
        │        │         │
        ▼        ▼         ▼
     🖥️ Apps   📁 Files   🌐 Web
        │        │         │
        └────────┼─────────┘
                 ▼
          ⚙️ Automation
                 │
                 ▼
          🔊 Assistant
             Response
```

---

# 🛠️ Technology Stack

| Technology        | Purpose               |
| ----------------- | --------------------- |
| Python            | Core development      |
| Streamlit         | User interface        |
| PyAutoGUI         | Desktop automation    |
| PyWin32           | Windows integration   |
| PyGetWindow       | Window management     |
| SpeechRecognition | Voice input           |
| Edge-TTS          | Text-to-speech        |
| Pygame            | Audio playback        |
| Webbrowser        | Browser automation    |
| Subprocess        | Application launching |
| Pathlib           | File management       |

---

# 📂 Project Structure

```text
newdesktopgenie/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── automation/
│   ├── __init__.py
│   ├── apps.py
│   ├── browser.py
│   ├── files.py
│   └── whatsapp.py
│
├── voice/
│   ├── __init__.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
└── ai/
    ├── __init__.py
    └── command_processor.py
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd newdesktopgenie
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If required, install the voice dependencies:

```bash
pip install SpeechRecognition edge-tts pygame
```

---

# ▶️ Running DesktopGenie

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🎯 Example Commands

### Applications

```text
Open Chrome
Open Calculator
Open Notepad
Open Explorer
Open Task Manager
Open Command Prompt
```

### Web

```text
Search Google for Python tutorials
Open YouTube
Open Gmail
Open GitHub
```

### Files

```text
Create a file named test.txt
Create a folder named Projects
Find my files
Open the Projects folder
Rename test.txt to demo.txt
```

### WhatsApp

```text
Open WhatsApp
```

```text
Message Sana Hello, how are you?
```

```text
Open WhatsApp and msg Sana Kaisi ho
```

---

# 🔐 Privacy & Security

DesktopGenie is designed with local desktop interaction in mind.

The assistant performs actions on the user's own computer and does not require uploading personal files to a remote server for basic desktop automation.

Future versions will introduce additional permission controls for sensitive operations.

> **Important:** Automation commands can directly interact with applications and files. Users should only run commands they understand and trust.

---

# 🏆 Hackathon Focus

DesktopGenie was developed as a hackathon project with a focus on:

### 🤖 AI

Making computer interaction more natural through conversational commands.

### ⚡ Automation

Reducing repetitive manual desktop tasks.

### 🎙️ Accessibility

Allowing users to interact with their computer through voice.

### 💡 Productivity

Combining multiple everyday tasks into one assistant.

### 🔮 Future-Ready Design

Building an architecture that can be extended with additional AI capabilities and automation skills.

---

# 🗺️ Future Roadmap

DesktopGenie is designed to grow beyond basic desktop automation.

## 🧠 Advanced AI Understanding

Integrate more powerful local or cloud-based LLMs to understand complex natural-language commands.

Example:

```text
"Open Chrome, search for today's AI news,
and open the first result."
```

---

## 🎙️ Multilingual Voice Support

Add support for:

* English
* Urdu
* Roman Urdu
* Additional languages

This would make DesktopGenie more accessible to a wider range of users.

---

## 👁️ Computer Vision

Enable DesktopGenie to understand what is visible on the screen.

Future capabilities could include:

* Detecting buttons
* Identifying icons
* Understanding UI layouts
* Reading screen content
* Clicking UI elements intelligently

---

## 🌐 Advanced Browser Automation

Extend browser automation to support:

* Form filling
* Website navigation
* Data extraction
* Repetitive web tasks
* Multi-step workflows

---

## 📱 More App Integrations

Future versions could integrate:

* Telegram
* Gmail
* Slack
* Microsoft Teams
* Discord
* Calendar applications

---

## 📅 Productivity Assistant

Add productivity features such as:

* Reminders
* Calendar events
* To-do lists
* Notes
* Timers
* Daily planning

---

## 🔐 Permission & Safety System

Introduce an intelligent permission layer.

For example:

```text
User: Delete this folder.

DesktopGenie:
⚠️ This action will permanently delete the folder.
Do you want to continue?

[Yes] [Cancel]
```

This would make automation safer.

---

## 🧩 Plugin Architecture

Allow developers to create custom DesktopGenie skills.

For example:

```text
skills/
├── spotify.py
├── email.py
├── calendar.py
└── coding.py
```

This would allow DesktopGenie to evolve into an extensible personal AI platform.

---

## 💻 Cross-Platform Support

Future versions could support:

* Windows
* Linux
* macOS

---

## ⚡ Background AI Assistant

DesktopGenie could eventually run in the background and activate using a wake word.

Example:

> **"Hey DesktopGenie..."**

---

# 🌟 Vision

The long-term vision of DesktopGenie is to create a **personal AI computer assistant** that can understand natural language, see what is happening on the screen, make decisions, and safely perform multi-step tasks on behalf of the user.

Instead of users learning how to operate software, the goal is to make software understand **how users want to work**.

> **From clicking buttons to simply telling your computer what you need.**

---

# 👩‍💻 Project

**Project:** DesktopGenie
**Category:** AI / Desktop Automation
**Platform:** Windows
**Interface:** Streamlit
**Language:** Python

---

# ⭐ Conclusion

DesktopGenie brings together **AI, voice interaction, desktop automation, file management, browser automation, and communication tools** into one practical assistant.

The current version focuses on reliable everyday automation, while the roadmap opens the door toward a more intelligent, multilingual, vision-enabled, and extensible personal AI assistant.

### 🚀 DesktopGenie — Your Computer, Your Voice, Your Assistant.
