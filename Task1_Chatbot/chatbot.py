# chatbot.py

responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm a bot, but I'm doing great! Thanks!",
    "bye": "Goodbye! Have a nice day.",
    "who are you": "I'm a simple chatbot created by you.",
    "what can you do": "I can answer your basic questions."
}

def chatbot():
    print("Welcome to ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Bot: Goodbye!")
            break
        elif user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
