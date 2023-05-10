def check(s):
    if s[0].isupper() == False:
        return False
    elif s[-1].isupper() == False:
        return False
    elif len(s) != 8:
        return False
    elif s[1:7].isdecimal() == False:
        return False
    elif int(s[1:7]) < 100000 or int(s[1:7]) > 999999:
        return False
    else:
        return True
s = input()

if __name__ == '__main__':
    check()