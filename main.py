from speech_recognition_module import listen
from nlp import process_text, interpret_command
from commands import execute_command

def main():
    while True:
        text = listen()
        if text:
            tokens = process_text(text)
            command = interpret_command(tokens)
            response = execute_command(command, text)
            print(response)  # Optional: Print the response for debugging

if __name__ == "__main__":
    main()
