# Simple Telegram Bot

Simple Telegram chatbot done with python/requests/telepot + aws ec2
Features:

- Direct message : word1->Text(word1)
- Random response on word : word->Text(phrase)
- Giphy fetch message : word->Document(random giphy tag-based)
- Polygen generator : word->Text(random polygen phrase)
- Xkcd random quote : word->Image(random Xkcd image)
- Reddit random photo : word->Image(random random image)

### Contributing

    text rules : app->modules->dictionary->language.py

    extensions : app->modules->*

### TODO

- Continuous delivery -> fabric/gitlab ci-cd
- NLTK
- Unittests
- Logs

## RUN

    pip install -r requirements.txt
    export BOT_API_KEY=xxxxxx
    export GIPHY_API_KEY=xxxxxx
    python main.py

## Built With

* [Python 3.6](https://www.python.org/downloads/release/python-360/) - lang
* [Requests](http://docs.python-requests.org/en/master/) - Http calls
* [Telepot](http://telepot.readthedocs.io/en/latest/) - Telegram bot helpers for python
