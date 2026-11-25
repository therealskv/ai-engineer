from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

print("Sending message to Claude...\n")

with client.messages.stream(
    model="claude-opus-4-6",
    max_tokens=1024,
    system="You are a helpful AI engineering mentor.",
    messages=[
        {"role": "user", "content": "In 3 sentences, what is the single most important thing a principal architect should understand about LLMs before building with them?"}
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

print("\n\nDone.")