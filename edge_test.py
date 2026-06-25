import asyncio
import edge_tts
import os

TEXT = "Hello Pragya. This is Edge TTS."

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        voice="en-US-JennyNeural"
    )

    await communicate.save("speech.mp3")

asyncio.run(main())

os.system("start speech.mp3")