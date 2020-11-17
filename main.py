import numpy as np


def loadWords(path='./words.txt'):
    words = open(path).read().splitlines()
    return words


def wordsToArray(words):
    return [list(word) for word in words]


def filterEqualLen(main, words):
    return [word for word in words if len(main) == len(word)]


def correct(word):
    # check if already in words
    if word in words:
        return word

    equalLenWords = filterEqualLen(word, words)

    wordsArr = np.array(wordsToArray(equalLenWords))

    mainArr = np.array(list(word))
    length = len(word)

    bitMatrix = (wordsArr == mainArr).astype(int)

    # shorter distance is predicted word//corrected
    distance = np.sum(np.ones(length) - bitMatrix, axis=1)
    closest = np.where(distance == distance.min())[0]

    predicted = [equalLenWords[close] for close in closest]

    # free memory...5MB
    del equalLenWords
    del wordsArr
    del bitMatrix

    return predicted


if __name__ == "__main__":
    # used https://github.com/dwyl/english-words
    words = loadWords()

    while True:
        word = input('Enter Word: ')
        if word == 'q':
            break
        print('Correct:', correct(word))

    del words
