import googletrans
from googletrans import Translator

supported_lang = ['fa','ru','de']

def eng_to_farsi_translate(text):

    translator = Translator()
    
    lang_detector = translator.detect(text).lang
    if lang_detector == 'fa':
        return text

    else:

        fa_translated = translator.translate(text , src='en',dest='fa').text
        return fa_translated
    