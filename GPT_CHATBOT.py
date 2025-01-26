import openai
import os

# Set your OpenAI API key as an environment variable and access it securely
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_gpt(prompt):
    """
    Sends a prompt to OpenAI's ChatCompletion API and returns the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"

def main():
    """
    Runs a chat loop where the user can interact with the chatbot.
    """
    print("Chatbot initialized. Type 'quit', 'exit', or 'bye' to end the chat.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print('Chatbot:', response)

if __name__ == '__main__':
    main()
