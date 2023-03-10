import googletrans
from googletrans import Translator

supported_lang = ['fa','ru','de']

def eng_translator(text):

    translator = Translator()
    
    lang_detector = translator.detect(text).lang
    if lang_detector not in supported_lang:
        return text
    else:

        translated = translator.translate(text , src='en',dest=lang_detector).text
        return translated
    