def findWord(word):
    if len(word) == 1:
        return ord(word) - 64
    else:
        count = 0
        for i in range(len(word)):
            count += (ord(word[i]) - 64) * 26 ** (len(word) - i - 1)
        return count

if __name__ == '__main__':
    findWord()