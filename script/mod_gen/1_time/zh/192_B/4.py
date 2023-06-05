def isDifficult(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if ord(s[i]) < 97:
                return False
        else:
            if ord(s[i]) > 96:
                return False
    return True
s = input()

if __name__ == '__main__':
    isDifficult()