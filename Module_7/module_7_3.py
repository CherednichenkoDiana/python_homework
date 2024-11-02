import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for file in file_names:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = dict()

        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                str = file.read().lower()
                str = re.sub(r'[^\w\s]', '', str)
                str = str.split()
                all_words[name] = str

        return all_words

    def find(self, word):
        res = dict()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.index(word.lower()) + 1
        return res

    def count(self, word):
        res = dict()
        for name, words in self.get_all_words().items():
            res[name] = words.count(word.lower())
        return res

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt', 'test_file2.txt')

    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.find('ПроверкА'))  # 1 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
