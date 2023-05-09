def getAnagramCount(word):
    wordSet = set(word)
    wordList = list(wordSet)
    wordList.sort()
    wordList.sort(key=len)
    wordList.reverse()
    return wordList
