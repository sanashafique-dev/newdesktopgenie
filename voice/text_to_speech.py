import asyncio
import edge_tts
import pygame
import os
import tempfile

VOICE = "en-US-AriaNeural"


async def generate_voice(text, output_file):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)


def speak(text):
    try:
        if not text:
            return False

        text = str(text).strip()

        output_file = os.path.join(
            tempfile.gettempdir(),
            "desktopgenie_voice.mp3"
        )

        asyncio.run(generate_voice(text, output_file))

        pygame.mixer.init()
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.quit()

        return True

    except Exception as e:
        print("TTS Error:", e)
        return False