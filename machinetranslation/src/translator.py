# Import the MyMemoryTranslator from the deep_translator package in your Python code
from deep_translator import MyMemoryTranslator

# Implement a method that translates the input text from English to French
def translate_to_french(text):
    """
    Translate the input text from English to French using the MyMemoryTranslator
    :param text: a string of English text
    :return: a string of French text
    """
    # create an instance of the MyMemoryTranslator with the source and target languages
    translator = MyMemoryTranslator(source="en", target="fr")
    # use the translate method to get the translation
    translation = translator.translate(text)
    # return the translation
    return translation

# Implement a method that translates the input text from French to English
def translate_to_english(text):
    """
    Translate the input text from French to English using the MyMemoryTranslator
    :param text: a string of French text
    :return: a string of English text
    """
    # create an instance of the MyMemoryTranslator with the source and target languages
    translator = MyMemoryTranslator(source="fr", target="en")
    # use the translate method to get the translation
    translation = translator.translate(text)
    # return the translation
    return translation
    