def isDifficult(str):
    for i in range(0,len(str),2):
        if str[i].islower():
            return False
    for i in range(1,len(str),2):
        if str[i].isupper():
            return False
    return True
str = input()

if __name__ == '__main__':
    isDifficult()