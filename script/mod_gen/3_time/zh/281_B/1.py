def check(s):
    if len(s) != 9:
        return False
    if s[0] < 'A' or s[0] > 'Z':
        return False
    if s[8] < 'A' or s[8] > 'Z':
        return False
    if not s[1:7].isdigit():
        return False
    if int(s[1:7]) < 100000 or int(s[1:7]) > 999999:
        return False
    return True
s = input()

if __name__ == '__main__':
    check()