from bs4 import BeautifulSoup
import requests


def get_polygen(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser').find(**{"class": "generation"}).text


if __name__ == "__main__":
    print(get_polygen("https://polygen.org/it/grammatiche/cultura/ita/prov.grm"))
