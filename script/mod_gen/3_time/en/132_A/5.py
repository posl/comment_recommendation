def check(s):
    if len(s) != 4:
        return False
    if s[0] == s[1] == s[2] == s[3]:
        return False
    if s[0] == s[1] and s[2] == s[3]:
        return True
    if s[0] == s[2] and s[1] == s[3]:
        return True
    if s[0] == s[3] and s[1] == s[2]:
        return True
    return False
s = input()

if __name__ == '__main__':
    check()