from app.modules.base import Module

# WIP
from app.modules.dictionary import language
from app.modules.photo.junkfood import get_junkfood_photo
from app.modules.photo.xkcd import get_xkcd_photo


class XkcdPhoto(Module):

    @staticmethod
    def resolver(processed):
        for word in processed:
            if word in language.xkcd_lang:
                return get_xkcd_photo()
        return None


class JunkfoodPhoto(Module):

    @staticmethod
    def resolver(processed):
        for word in processed:
            if word in language.foodporn_lang:
                return get_junkfood_photo()
        return None
