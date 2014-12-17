import csv
import random
from string import ascii_uppercase

def remove_non_ascii(s):
    return "".join(i for i in s if ord(i)<128)

class WordDictionary(object):

    def __init__(self, filename):
        self.words = {}
        self.load_words(filename)

    def load_words(self, filename):
        self.words = {}

        with open(filename, 'rb') as f:
            r = csv.reader(f)

            for line in r:
                word = remove_non_ascii(line[1]).upper()
                self.words[word] = 1

        return True

    def is_valid_word(self, word):
        # TODO
        pass

class GameBoard(object):

    def __init__(self, N=10):
        self.N = N
        letters = ascii_uppercase
        self.board = [[random.choice(letters) for _ in xrange(N)] for _ in xrange(N)]

    def print_board(self):
        # this is useful for testing
        for i in xrange(self.N):
            print ''
            for j in xrange(self.N):
                print self.board[i][j],


def get_word_dict():
    wd = WordDictionary('words.csv')
    return wd

