import random
from bs4 import BeautifulSoup
import requests


def get_xkcd_photo(index=None):
    idx = index or random.randint(0, 1900)
    r = requests.get("https://xkcd.com/{}/".format(idx))

    return get_image(r.text)


def get_image(html_doc):
    obj = BeautifulSoup(html_doc, 'html.parser')
    return "http:"+obj.find(id="comic").find('img').get('src')


if __name__ == "__main__":
    print(get_xkcd_photo())
