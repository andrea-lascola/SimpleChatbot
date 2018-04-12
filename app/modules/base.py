from functools import partial


class Module(object):
    formatters = [
        str.lower,
        partial(lambda x: x.replace("?", "")),
        partial(lambda x: x.replace("!", "")),
        partial(lambda x: x.replace(".", "")),
        partial(lambda x: x.replace(",", ""))
    ]

    @staticmethod
    def processor(_input):
        words = _input.split(" ")

        for func in Module.formatters:
            words = map(func, words)

        return words

    @staticmethod
    def resolver(processed):
        pass
