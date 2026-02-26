chat_history = []

print("Command Bot Started (type 'help' to see commands)")
print("Type 'exit' to stop\n")

while True:
    user_input = input("You: ").strip().lower()
    chat_history.append(user_input)

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    elif user_input == "help":
        print("""
Available Commands:
- hello
- about
- time
- history
- clear
- exit
""")

    elif user_input == "hello":
        print("Bot: Hello Yoges!")

    elif user_input == "about":
        print("Bot: I am a command-based chatbot built in Python.")

    elif user_input == "time":
        import datetime
        now = datetime.datetime.now()
        print("Bot: Current time is", now.strftime("%H:%M:%S"))

    elif user_input == "history":
        print("\n--- Chat History ---")
        for msg in chat_history:
            print(msg)
        print("--------------------")

    elif user_input == "clear":
        chat_history.clear()
        print("Bot: Chat history cleared.")

    else:
        print("Bot: Sorry, I don't understand that command.")