import json
import os
from deep_translator import MyMemoryTranslator

def translate_english_to_french(text):
    translator = MyMemoryTranslator(source='en', target='fr')
    translation = translator.translate(text)
    return translation