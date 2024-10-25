#!/usr/bin/python3

from greetings import Greetings

def main():
    language = input("Enter the language (default: english): ")

    prompt, language, exit_words = Greetings.setup_language(language)

    if prompt is not None:
        while True:
            original_input = input(prompt)
            x              = original_input.casefold()

            if x in exit_words:
                break

            result = Greetings.check_string(original_input, language)

            print(result)

if __name__ == '__main__':
    main()
