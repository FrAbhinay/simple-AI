import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you ?', ['I am fine, thank you!', 'Fine, thanks!', 'Good!']],
    ['what is your name ?', ['I am a chatbot created with Python!', 'You can call me Chatbot.']],
    ['(.*) your name ?', ['My name is Chatbot.']],
    ['(.*) help (.*)', ['I can help you with various things. How can I assist you?']],
    ['(.*) thank you (.*)', ['You\'re welcome!', 'No problem.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']],
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Define a function to start the chatbot
def chatbot_response(input_text):
    return chatbot.respond(input_text)

# Main function to run the chatbot
def main():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if user_input.lower() == 'bye':
            break

if __name__ == "__main__":
    main()
