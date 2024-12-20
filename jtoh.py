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
            for i in range(len(self.get_all_words()[name])):
                if word.lower() == self.get_all_words()[name][i].lower():
                    a = i + 1
                    break
            hi[name] = a
        return hi
    def count(self, word):
        hi = {}
        for name in self.names:
            a = 0
            for i in range(len(self.get_all_words()[name])):
                 if word.lower() == self.get_all_words()[name][i].lower():
                    a += 1
            hi[name] = a
        return hi
