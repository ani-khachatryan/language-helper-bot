import googletrans
from googletrans import Translator


all_lang = googletrans.LANGUAGES
langcodes = dict(map(reversed,all_lang.items()))
translator = Translator()

def check_if_lang(lang):
    if lang in langcodes.values():
        return lang
    elif lang in langcodes.keys():
        return langcodes[lang]
    else:
        return False

def translate(text, to = 'en'):
    return translator.translate(text, dest = to).text
