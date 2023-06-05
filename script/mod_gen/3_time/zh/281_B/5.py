def check(s):
    if s[0] < 'A' or s[0] > 'Z':
        return False
    if s[-1] < 'A' or s[-1] > 'Z':
        return False
    if len(s) != 8:
        return False
    if s[1:7].isdigit() == False:
        return False
    if int(s[1:7]) < 100000 or int(s[1:7]) > 999999:
        return False
    return True
s = input()

if __name__ == '__main__':
    check()