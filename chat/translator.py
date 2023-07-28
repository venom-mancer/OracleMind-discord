import googletrans
from googletrans import Translator

supported_lang = ['fa']

def eng_translator(text):

    translator = Translator()
    
    lang_detector = translator.detect(text).lang
    if lang_detector in supported_lang:
        return text
    else:

        translated = translator.translate(text , src='en',dest=supported_lang[0]).text
        return translated
    