def check(s):
    for i in range(len(s)):
        if i%2 == 0:
            if s[i].islower() == False:
                return False
        else:
            if s[i].isupper() == False:
                return False
    return True
s = input()

if __name__ == '__main__':
    check()