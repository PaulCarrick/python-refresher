from greetings import Greetings as gr

def test_setup_default_language_function():
    prompt, language, exit_words = gr.setup_language()
    assert prompt == "Please enter a salutation or valediction (or quit / done to exit): "
    assert language == "english"
    assert exit_words == ["quit", "done"]

def test_setup_english_language_function():
    prompt, language, exit_words = gr.setup_language("english")
    assert prompt == "Please enter a salutation or valediction (or quit / done to exit): "
    assert language == "english"
    assert exit_words == ["quit", "done"]

def test_setup_spanish_language_1_function():
    prompt, language, exit_words = gr.setup_language("spanish")
    assert prompt == "Por favor, ingrese un saludo o una despedida (o alto / terminado para salir): "
    assert language == "spanish"
    assert exit_words == ["alto", "terminado"]

def test_setup_spanish_language_2_function():
    prompt, language, exit_words = gr.setup_language("espanol")
    assert prompt == "Por favor, ingrese un saludo o una despedida (o alto / terminado para salir): "
    assert language == "espanol"
    assert exit_words == ["alto", "terminado"]

def test_setup_french_language_1_function():
    prompt, language, exit_words = gr.setup_language("french")
    assert prompt == "Veuillez entrer une salutation ou une formule de politesse (ou quitter / fait sortir): "
    assert language == "french"
    assert exit_words == ["quitter", "fait"]

def test_setup_french_language_2_function():
    prompt, language, exit_words = gr.setup_language("francais")
    assert prompt == "Veuillez entrer une salutation ou une formule de politesse (ou quitter / fait sortir): "
    assert language == "francais"
    assert exit_words == ["quitter", "fait"]

def test_english_greetings_function():
    response = gr.check_english_string('hello')
    assert response == "The greeting is \"hello\"."
    response = gr.check_english_string('Hello')
    assert response == "The greeting is \"Hello\"."
    response = gr.check_english_string('HELLO')
    assert response == "The greeting is \"HELLO\"."
    response = gr.check_english_string('hi')
    assert response == "The greeting is \"hi\"."
    response = gr.check_english_string('Hi')
    assert response == "The greeting is \"Hi\"."
    response = gr.check_english_string('HI')
    assert response == "The greeting is \"HI\"."
    response = gr.check_english_string('howdy')
    assert response == "The greeting is \"howdy\"."
    response = gr.check_english_string('Howdy')
    assert response == "The greeting is \"Howdy\"."
    response = gr.check_english_string('HOWDY')
    assert response == "The greeting is \"HOWDY\"."

def test_english_valedictions_function():
    response = gr.check_english_string('goodbye')
    assert response == "The valediction is \"goodbye\"."
    response = gr.check_english_string('Goodbye')
    assert response == "The valediction is \"Goodbye\"."
    response = gr.check_english_string('GOODBYE')
    assert response == "The valediction is \"GOODBYE\"."
    response = gr.check_english_string('bye')
    assert response == "The valediction is \"bye\"."
    response = gr.check_english_string('Bye')
    assert response == "The valediction is \"Bye\"."
    response = gr.check_english_string('BYE')
    assert response == "The valediction is \"BYE\"."
    response = gr.check_english_string('so long')
    assert response == "The valediction is \"so long\"."
    response = gr.check_english_string('So Long')
    assert response == "The valediction is \"So Long\"."
    response = gr.check_english_string('SO LONG')
    assert response == "The valediction is \"SO LONG\"."

def test_english_unknown_function():
    response = gr.check_english_string('unknown')
    assert response == "\"unknown\" is not a greeting or valediction."
    response = gr.check_english_string('Unknown')
    assert response == "\"Unknown\" is not a greeting or valediction."
    response = gr.check_english_string('UNKNOWN')
    assert response == "\"UNKNOWN\" is not a greeting or valediction."

def test_spanish_greetings_function():
    response = gr.check_spanish_string('hola')
    assert response == "El saludo es \"hola\"."
    response = gr.check_spanish_string('Hola')
    assert response == "El saludo es \"Hola\"."
    response = gr.check_spanish_string('HOLA')
    assert response == "El saludo es \"HOLA\"."
    response = gr.check_spanish_string('buenos días')
    assert response == "El saludo es \"buenos días\"."
    response = gr.check_spanish_string('Buenos Días')
    assert response == "El saludo es \"Buenos Días\"."
    response = gr.check_spanish_string('BUENOS DÍAS')
    assert response == "El saludo es \"BUENOS DÍAS\"."
    response = gr.check_spanish_string('buenos noches')
    assert response == "El saludo es \"buenos noches\"."
    response = gr.check_spanish_string('Buenos Noches')
    assert response == "El saludo es \"Buenos Noches\"."
    response = gr.check_spanish_string('BUENOS NOCHES')
    assert response == "El saludo es \"BUENOS NOCHES\"."

def test_spanish_valedictions_function():
    response = gr.check_spanish_string('adios')
    assert response == "La despedida es \"adios\"."
    response = gr.check_spanish_string('Adios')
    assert response == "La despedida es \"Adios\"."
    response = gr.check_spanish_string('ADIOS')
    assert response == "La despedida es \"ADIOS\"."
    response = gr.check_spanish_string('hasta luego')
    assert response == "La despedida es \"hasta luego\"."
    response = gr.check_spanish_string('Hasta Luego')
    assert response == "La despedida es \"Hasta Luego\"."
    response = gr.check_spanish_string('HASTA LUEGO')
    assert response == "La despedida es \"HASTA LUEGO\"."
    response = gr.check_spanish_string('hasta pronto')
    assert response == "La despedida es \"hasta pronto\"."
    response = gr.check_spanish_string('Hasta Pronto')
    assert response == "La despedida es \"Hasta Pronto\"."
    response = gr.check_spanish_string('HASTA PRONTO')
    assert response == "La despedida es \"HASTA PRONTO\"."
    response = gr.check_spanish_string('hasta manana')
    assert response == "La despedida es \"hasta manana\"."
    response = gr.check_spanish_string('Hasta Manana')
    assert response == "La despedida es \"Hasta Manana\"."
    response = gr.check_spanish_string('HASTA MANANA')
    assert response == "La despedida es \"HASTA MANANA\"."
    response = gr.check_spanish_string('hasta manana')
    assert response == "La despedida es \"hasta manana\"."
    response = gr.check_spanish_string('Hasta Manana')
    assert response == "La despedida es \"Hasta Manana\"."
    response = gr.check_spanish_string('HASTA MANANA')
    assert response == "La despedida es \"HASTA MANANA\"."
    response = gr.check_spanish_string('nos vemos')
    assert response == "La despedida es \"nos vemos\"."
    response = gr.check_spanish_string('Nos Vemos')
    assert response == "La despedida es \"Nos Vemos\"."
    response = gr.check_spanish_string('NOS VEMOS')
    assert response == "La despedida es \"NOS VEMOS\"."

def test_spanish_unknown_function():
    response = gr.check_spanish_string('unknown')
    assert response == "\"unknown\" no es un saludo ni una despedida."
    response = gr.check_spanish_string('Unknown')
    assert response == "\"Unknown\" no es un saludo ni una despedida."
    response = gr.check_spanish_string('UNKNOWN')
    assert response == "\"UNKNOWN\" no es un saludo ni una despedida."

def test_french_greetings_function():
    response = gr.check_french_string('salut')
    assert response == "La salutation est \"salut\"."
    response = gr.check_french_string('Salut')
    assert response == "La salutation est \"Salut\"."
    response = gr.check_french_string('SALUT')
    assert response == "La salutation est \"SALUT\"."
    response = gr.check_french_string('bonjour')
    assert response == "La salutation est \"bonjour\"."
    response = gr.check_french_string('Bonjour')
    assert response == "La salutation est \"Bonjour\"."
    response = gr.check_french_string('BONJOUR')
    assert response == "La salutation est \"BONJOUR\"."
    response = gr.check_french_string('bonne nuit')
    assert response == "La salutation est \"bonne nuit\"."
    response = gr.check_french_string('Bonne Nuit')
    assert response == "La salutation est \"Bonne Nuit\"."
    response = gr.check_french_string('BONNE NUIT')
    assert response == "La salutation est \"BONNE NUIT\"."

def test_french_valedictions_function():
    response = gr.check_french_string('au revoir')
    assert response == "La formule de politesse est \"au revoir\"."
    response = gr.check_french_string('Au Revoir')
    assert response == "La formule de politesse est \"Au Revoir\"."
    response = gr.check_french_string('AU REVOIR')
    assert response == "La formule de politesse est \"AU REVOIR\"."
    response = gr.check_french_string('a plus tard')
    assert response == "La formule de politesse est \"a plus tard\"."
    response = gr.check_french_string('A Plus Tard')
    assert response == "La formule de politesse est \"A Plus Tard\"."
    response = gr.check_french_string('A PLUS TARD')
    assert response == "La formule de politesse est \"A PLUS TARD\"."
    response = gr.check_french_string('a plus')
    assert response == "La formule de politesse est \"a plus\"."
    response = gr.check_french_string('A Plus')
    assert response == "La formule de politesse est \"A Plus\"."
    response = gr.check_french_string('A PLUS')
    assert response == "La formule de politesse est \"A PLUS\"."

def test_french_unknown_function():
    response = gr.check_french_string('unknown')
    assert response == "\"unknown\" n'est pas une salutation ni une formule de politesse."
    response = gr.check_french_string('Unknown')
    assert response == "\"Unknown\" n'est pas une salutation ni une formule de politesse."
    response = gr.check_french_string('UNKNOWN')
    assert response == "\"UNKNOWN\" n'est pas une salutation ni une formule de politesse."
