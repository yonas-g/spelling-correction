# assuming there is an array of words converted to 2D array of letters
# 1. remove not equal length
# 2. build bit matrix of existence


def maxLengthWord(words):
    maxLen = 0
    for word in words:
        if len(word) > maxLen:
            maxLen = len(word)

    return maxLen


def fillLen(word1, word2):
    # both list array
    len1 = len(word1)
    len2 = len(word2)

    fillLen = abs(len1 - len2)
    fillChar = ' '*fillLen

    # fill with empty char
    if len1 > len2:
        word2.extend(fillChar)
    else:
        word1.extend(fillChar)

    return word1, word2


def loadWords():
    words = open('./words.txt').read().splitlines()
    return words


words = [
    'clearing',
    'dealing',
    'brushing',
    'cleaning',
    'drilling',
    'cleening',
    'clean'
]

# correct this to 'cleaning'
main = 'c1eaning'
mainArr = list(main)
length = len(main)


print(loadWords()[:10])

# memory size
# size = (sys.getsizeof(equalLenWords) + sys.getsizeof(wordsArr) +
#             sys.getsizeof(bitMatrix) + sys.getsizeof(words))/1000
