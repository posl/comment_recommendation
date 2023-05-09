def check(s):
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        return "Yes"
    elif s[0] == s[2] and s[1] == s[3] and s[0] != s[1]:
        return "Yes"
    elif s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    check()