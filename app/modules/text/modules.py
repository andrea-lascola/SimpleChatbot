import random

from app.modules.base import Module
from app.modules.dictionary import language
from app.modules.text.polygen import get_polygen

direct_dictionary = {
}


class DirectAssociation(Module):
    @staticmethod
    def resolver(processed):
        for word in processed:
            if word in direct_dictionary:
                return direct_dictionary[word]
        return None


class Chooser(Module):
    @staticmethod
    def resolver(processed):
        for word in processed:
            if word in language.choose_lang:
                return random.choice(language.choose_lang[word])
        return None

class Polygen(Module):
    @staticmethod
    def resolver(processed):
        for word in processed:
            for words, link in language.polygen:
                if word in words:
                    return get_polygen(link)
        return None
