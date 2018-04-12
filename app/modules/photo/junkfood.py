from bs4 import BeautifulSoup
import requests


def get_junkfood_photo():
    r = requests.get("https://www.reddit.com/r/FoodPorn/random")

    return get_image(r.text)


def get_image(html_doc):
    obj = BeautifulSoup(html_doc, 'html.parser')
    return obj.find(**{"data-event-action": "title"}).get('data-href-url')


if __name__ == "__main__":
    print(get_junkfood_photo())
