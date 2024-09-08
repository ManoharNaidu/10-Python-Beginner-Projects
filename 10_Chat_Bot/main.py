from difflib import SequenceMatcher
from datetime import datetime

class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    def get_best_response(self, user_input: str) -> tuple[str, float]:
        highest_similarity = 0.0
        best_response = "I'm sorry, I didn't understand that. Can you please rephrase?"

        for response in self.responses:
            similarity = self.calculate_similarity(user_input, response)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_response = self.responses[response]

        return best_response, highest_similarity

    def calculate_similarity(self, user_input: str, response: str) -> float:
        # Dummy similarity calculation for demonstration purposes
        return 1.0 if user_input.lower() == response.lower() else 0.0

    def run(self) -> None:
        print(f"{self.name}: Hi, I'm {self.name}. How can I help you?")
        while True:
            user_input: str = input("You: ")
            if user_input.lower() == "exit":
                print(f"{self.name}: Goodbye!")
                break

            response, similarity = self.get_best_response(user_input)

            if similarity < 0.5:
                response = "I'm sorry, I didn't understand that. Can you please rephrase?"
            elif response == "GET_TIME":
                response = datetime.now().strftime("%H:%M:%S")
            
            print(f"{self.name}: {response} (Similarity: {similarity:.2%})")

def main() -> None:
    responses: dict[str, str] = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm an AI, so I don't have feelings, but I'm here to help you!",
        "what's your name": "I'm ChatBot, your virtual assistant.",
        "what time is it": "GET_TIME",
        "what is your purpose": "I'm here to assist you with any questions or tasks you have.",
        "who created you": "I was created by a team of developers.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the capital of France": "The capital of France is Paris.",
        "how do you work": "I use artificial intelligence to understand and respond to your queries.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! If you have any other questions, feel free to ask."
    }
    chat_bot: ChatBot = ChatBot("ChatBot", responses)
    chat_bot.run()

if __name__ == "__main__":
    main()