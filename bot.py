print("Bot: Hi! Main tumhara chatbot hu. Baat karne ke liye kuch type karo (exit karne ke liye 'bye' likho).")
while True:
    user_input = input("Aap: ").lower()
    words = user_input.split()
    
    if "bye" in words:
        print("Bot: Bye bye! Take care!")
        break
    elif "hi" in words or "hello" in words:
        print("Bot: Hello! Kaise ho?")
    elif "what is your name" in user_input:
        print("Bot: My name is Bot.")
    elif "how are you?" in user_input:
        print("Bot: I am good and What about you?")
    elif "thank you" in user_input:
        print("Bot: Your Welcome")
    elif "help" in words:
        print("Bot: Main tumse baat kar sakta hu — try 'hi', 'name', 'how are you', 'bye', 'thanks'")
    else:
        print("Bot: Samjha nahi, thoda alag se pucho.")