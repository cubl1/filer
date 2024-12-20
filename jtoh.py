import string
class WordsFinder:
    def __init__(self, *filenames):
        self.names = list(filenames)
    def get_all_words(self):
        all_words = {}
        for name in self.names:
            with open(name, "r") as file:
                all_words[name] = list(file.read().translate(str.maketrans(' ', ' ', string.punctuation)).split())
        return all_words
    def find(self, word):
        hi = {}
        for name in self.names:
            a = 0
            with open(name, "r") as file:
                words = list(file.read().translate(str.maketrans(' ', ' ', string.punctuation)).split())
                for i in range(len(words)):
                    if word.lower() == words[i].lower():
                        a = i + 1
                        break
                hi[name] = a
        return hi
    def count(self, word):
        hi = {}
        for name in self.names:
            a = 0
            with open(name, "r") as file:
                words = list(file.read().translate(str.maketrans(' ', ' ', string.punctuation)).split())
                for i in range(len(words)):
                    if word.lower() == words[i].lower():
                        a += 1
                hi[name] = a
        return hi