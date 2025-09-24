# chatbot_openai.py
import os
from openai import OpenAI

class OpenAIChatbot:
    """
    A simple wrapper chatbot that talks to OpenAI Chat Completions.
    """
    def __init__(self, model="gpt-4o", system_prompt="You are a helpful assistant."):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set. Set it before running.")
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.messages = [{"role": "system", "content": system_prompt}]

    def get_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages
            )
            # robust extraction (works if response objects/dicts differ)
            choice = response.choices[0]
            try:
                assistant_response = choice.message.content
            except Exception:
                try:
                    assistant_response = choice['message']['content']
                except Exception:
                    assistant_response = str(response)
            self.messages.append({"role": "assistant", "content": assistant_response})
            return assistant_response
        except Exception as e:
            print(f"API error: {e}")
            # remove last user message if failed
            if self.messages and self.messages[-1]["role"] == "user":
                self.messages.pop()
            return "Sorry, I encountered an error. Please try again."

    def start_chat_cli(self):
        print("Chatbot initialized. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() == "exit":
                print("Goodbye!")
                break
            print("Bot:", self.get_response(user_input))

if __name__ == "__main__":
    legal_assistant_prompt = (
        "You are a helpful legal assistant. Provide clear, concise information on legal topics, "
        "but always remind the user to consult with a qualified lawyer for legal advice."
    )
    bot = OpenAIChatbot(system_prompt=legal_assistant_prompt)
    bot.start_chat_cli()
