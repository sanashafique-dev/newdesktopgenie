
import speech_recognition as sr


def listen():
    """
    Microphone se user ki voice sunta hai
    aur speech ko text mein convert karta hai.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        print("🔄 Converting speech to text...")

        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        print(f"🗣️ You said: {text}")

        return text

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        return ""

    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
        return ""

    except Exception as e:
        print(f"Voice error: {e}")
        return ""


def speech_to_text():
    """
    Compatibility function.
    """

    return listen()

