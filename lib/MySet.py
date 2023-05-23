import ipdb


class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()
        return self

    def __str__(self):
        values = list(self.dictionary.keys())
        values.sort()  # Sort the values for consistent output
        return f"MySet: {{{','.join(map(str, values))}}}"
