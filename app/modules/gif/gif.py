from app.modules.base import Module
from app.modules.dictionary import language
from app.modules.gif.utils import get_random_gif


# make categories configurable

class FoodGiphy(Module):

    @staticmethod
    def resolver(processed):
        for word in processed:
            if word in language.giphy_lang:
                return get_random_gif(
                    [
                        "food",
                        "chocolate"
                    ]
                )
        return None


class RageGif(Module):

    @staticmethod
    def resolver(processed):
        for word in processed:
            if word in language.giphy_rage_lang:
                return get_random_gif(
                    [
                        "machine gun",
                        "explosion",
                        "rage"
                    ]
                )
        return None
