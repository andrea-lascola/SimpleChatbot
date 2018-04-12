import random

import requests

from app.constants import giphy_url, giphy_api_key

rating = "G"  # Todo verify


def get_random_gif(tags):
    r = requests.get(giphy_url,
                     params=dict(
                         api_key=giphy_api_key,
                         tag=random.choice(tags),
                         rating=rating
                     ))
    response = r.json()
    return response["data"]["image_original_url"]
