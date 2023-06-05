def isHardRead(s):
    isHard = True
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].islower() == True:
                isHard = False
        else:
            if s[i].isupper() == True:
                isHard = False
    return isHard

if __name__ == '__main__':
    isHardRead()