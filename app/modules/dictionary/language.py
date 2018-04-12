# Example data -> todo fill

# Images
xkcd_lang = {
    "nerd"
}
foodporn_lang = {
    "foodporn"
}

# Giphy
giphy_lang = {
    "giphy"
}
giphy_rage_lang = {
    "rage",
}

# Talk

## Polygen

polygen = (
    ({"proverbi", "proverbio"},
     "https://polygen.org/it/grammatiche/cultura/ita/prov.grm"),
    ({"metal", "metallo", "musica"},
     "https://polygen.org/it/grammatiche/musica_cinema_e_spettacolo/eng/metal.grm"),
    ({"pattern", "design", "patterns"},
     "https://polygen.org/it/grammatiche/tecnologie/eng/designpatterns.grm"),
    ({"informatica", "informatico", "developer", "sviluppatore", "dev", "development", "develop", "programmatore"},
     "https://polygen.org/it/grammatiche/tecnologie/ita/genio.grm"),
    ({"manager", "pm", "pmo"},
     "https://polygen.org/it/grammatiche/tecnologie/eng/manager.grm"),
    ({"videogame", "videogames", "gaming", "game", "gioco", "ps4", "ps3", "ps"},
     "https://polygen.org/it/grammatiche/tecnologie/eng/videogames.grm"),
    ({"cocktail", "drink", "bere", "alchool", "alcool", "bevi", "bevete", "beviamo", "bevo"},
     "https://polygen.org/it/grammatiche/costume_e_societa/ita/cocktail.grm")
)

## Random
choose_lang = {
    "word": [
        "response1",
        "response2",
        "response3",
        "response4"
    ],
    "world": [
        "saturn",
        "jupiter",
        "sun",
        "venus",
        "moon",
        "pluto",
        "neptune"
    ]
}

aliases = {
    "world": ("planet","earth"),
    "word": ("word1","word2")
}


def copy_key(k1, k2):
    choose_lang[k1] = choose_lang[k2]


[copy_key(x, key) for key, values in aliases.items() for x in values]
