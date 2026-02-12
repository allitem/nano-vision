from googletrans import Translator

def translate(text, lang="en"):
    t = Translator()
    return t.translate(text, dest=lang).text
