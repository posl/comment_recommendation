def check(s):
    if len(s) != 7:
        return False
    if s[0] < "A" or "Z" < s[0]:
        return False
    if s[6] < "A" or "Z" < s[6]:
        return False
    if int(s[1:6]) < 100000 or 999999 < int(s[1:6]):
        return False
    return True
s = input()

if __name__ == '__main__':
    check()