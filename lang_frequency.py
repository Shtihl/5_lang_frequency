import re
import sys
from collections import Counter


def load_text_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    words_count = 10
    return Counter(words).most_common(words_count)


if __name__ == '__main__':
    document = load_text_data(sys.argv[1])
    for word, quantity in get_most_frequent_words(document):
        print('The word "{}" repeats {} times'.format(word, quantity))
