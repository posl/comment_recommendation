def isDifficult(word):
    for i in range(len(word)):
        if i % 2 == 0:
            if not word[i].islower():
                return False
        else:
            if not word[i].isupper():
                return False
    return True
word = input()

if __name__ == '__main__':
    isDifficult()