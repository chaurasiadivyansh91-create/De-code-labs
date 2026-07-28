print("AI Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am doing great! Thanks for asking.")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
