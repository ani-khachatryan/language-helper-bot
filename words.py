import nltk
from nltk.corpus import wordnet


def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())
    return ', '.join(set([el.replace("_", " ") for el in synonyms]))

def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            if i.antonyms():
                antonyms.append(i.antonyms()[0].name())
    return ', '.join(set([el.replace("_", " ") for el in antonyms]))
