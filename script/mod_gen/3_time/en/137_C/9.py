def getAnagramCount(s):
    anagramCount = 0
    anagramDict = dict()
    for i in range(len(s)):
        sortedString = ''.join(sorted(s[i]))
        if sortedString not in anagramDict:
            anagramDict[sortedString] = 1
        else:
            anagramDict[sortedString] += 1
            anagramCount += anagramDict[sortedString]
    return anagramCount

if __name__ == '__main__':
    getAnagramCount()