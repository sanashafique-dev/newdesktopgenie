
import webbrowser
from urllib.parse import quote_plus


# =========================================================
# GOOGLE SEARCH
# =========================================================

def google_search(query):
    """Search Google for the given query."""

    query = query.strip()

    if not query:
        return "Please provide something to search for."

    url = f"https://www.google.com/search?q={quote_plus(query)}"

    webbrowser.open(url)

    return f"Searching Google for: {query}"


# =========================================================
# OPEN WEBSITE
# =========================================================

def open_website(site):
    """Open a known website."""

    site = site.lower().strip()

    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "gmail": "https://mail.google.com",
        "github": "https://github.com",
        "whatsapp": "https://web.whatsapp.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "linkedin": "https://www.linkedin.com",
        "chatgpt": "https://chatgpt.com",
    }

    if site in websites:
        webbrowser.open(websites[site])
        return f"Opening {site.title()}"

    # If user gives a complete URL
    if site.startswith("http://") or site.startswith("https://"):
        webbrowser.open(site)
        return f"Opening {site}"

    # Try adding https:// for normal domains
    if "." in site:
        url = f"https://{site}"
        webbrowser.open(url)
        return f"Opening {site}"

    return f"I don't know that website: {site}"


# =========================================================
# OPEN WHATSAPP
# =========================================================

def open_whatsapp():
    """Open WhatsApp Web."""

    webbrowser.open("https://web.whatsapp.com")

    return "WhatsApp Web opened successfully."


# =========================================================
# OPEN YOUTUBE
# =========================================================

def open_youtube():
    """Open YouTube."""

    webbrowser.open("https://www.youtube.com")

    return "YouTube opened successfully."


# =========================================================
# OPEN GMAIL
# =========================================================

def open_gmail():
    """Open Gmail."""

    webbrowser.open("https://mail.google.com")

    return "Gmail opened successfully."

