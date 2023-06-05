def check(s):
    if len(s) < 2:
        return False
    if len(s) % 2 != 0:
        return False
    if s[0].isupper() == False:
        return False
    if s[-1].islower() == False:
        return False
    for i in range(1, len(s)-1):
        if i % 2 != 0:
            if s[i].isupper() == True:
                return False
        else:
            if s[i].islower() == True:
                return False
    return True
s = input()

if __name__ == '__main__':
    check()