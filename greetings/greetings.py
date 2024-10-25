"""Python refresher Greetings."""
class Greetings:
    """Class handlees greetings."""
    @staticmethod
    def check_string(original_text, language = "english"):
        """Function Check a string to see if it is a greeting."""
        match language.casefold():
            case "english":
                result = Greetings.check_english_string(original_text)

            case "spanish" | "espanol":
                result = Greetings.check_spanish_string(original_text)

            case "french" | "francais":
                result = Greetings.check_french_string(original_text)

            case _:
                result = f"Unknown language: {language}."

        return result


    @staticmethod
    def check_english_string(original_text):
        """Function Check a string to see if it is a greeting in English."""
        text = original_text.casefold()

        match text:
            case "hello" | "hi" | "howdy":
                result = f"The greeting is \"{original_text}\"."
            case "goodbye" | "bye" | "so long":
                result = f"The valediction is \"{original_text}\"."
            case _:
                result = f"\"{original_text}\" is not a greeting or valediction."

        return result


    @staticmethod
    def check_spanish_string(original_text):
        """Function Check a string to see if it is a greeting in Spanish."""
        text = original_text.casefold()

        match text:
            case "hola" | "buenos días" | "buenos noches":
                result = f"El saludo es \"{original_text}\"."
            case "adios" | "hasta luego" | "hasta pronto" | "hasta manana" | "nos vemos" |\
                 "via con dios":
                result = f"La despedida es \"{original_text}\"."
            case _:
                result = f"\"{original_text}\" no es un saludo ni una despedida."

        return result

    @staticmethod
    def check_french_string(original_text):
        """Function Check a string to see if it is a greeting in French."""
        text = original_text.casefold()

        match text:
            case "salut" | "bonjour" | "bonne nuit":
                result = f"La salutation est \"{original_text}\"."
            case "au revoir" | "a plus tard" | "a plus":
                result = f"La formule de politesse est \"{original_text}\"."
            case _:
                result = f"\"{original_text}\"\
 n\'est pas une salutation ni une formule de politesse."

        return result


    @staticmethod
    def setup_language(language = "english"):
        """Function Set up the language used."""
        prompt     = None
        exit_words = None

        if len(language) == 0:
            language = "english"

        match language.casefold():
            case "english":
                exit_words = ["quit", "done"]
                prompt     = f"Please enter a salutation or valediction \
(or {" / ".join(exit_words)} to exit): "

            case "spanish" | "espanol":
                exit_words = ["alto", "terminado"]
                prompt = f"Por favor, ingrese un saludo o una despedida \
(o {" / ".join(exit_words)} para salir): "

            case "french" | "francais":
                exit_words = ["quitter", "fait"]
                prompt = f"Veuillez entrer une salutation ou une formule de politesse \
(ou {" / ".join(exit_words)} sortir): "

            case _:
                print(f"Unknown language: {language}.")

        return prompt, language, exit_words
