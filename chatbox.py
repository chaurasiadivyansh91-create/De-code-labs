print("=" * 40)
print("🤖 Welcome to Rule-Based AI Chatbot")
print("Type 'exit' to end the chat.")
print("=" * 40)

while True:
    user = input("\nYou: ").strip().lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is Rule-Based AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created by Divyansh Chaurasia using Python.")

    elif user == "what can you do":
        print("Bot: I can greet you, answer simple questions, and chat using rule-based logic.")

    elif user == "time":
        from datetime import datetime
        print("Bot: Current time is", datetime.now().strftime("%I:%M %p"))

    elif user == "date":
        from datetime import date
        print("Bot: Today's date is", date.today())

    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")

