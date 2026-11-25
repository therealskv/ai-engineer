import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()
history = []

def chat(user_input: str) -> str:
    history.append({"role": "user", "content": user_input})
    response = client.messages.create(
        model="claude-haiku-4-5",      # Haiku for a chat loop — fast and cheap
        max_tokens=1024,
        system="You are a helpful assistant.",
        messages=history
    )
    
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply

def main():
    print("Chat started. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("quit", "exit"):
            break
        if not user_input:
            continue
        reply = chat(user_input)
        print(f"\nClaude: {reply}\n")

if __name__ == "__main__":
    main()