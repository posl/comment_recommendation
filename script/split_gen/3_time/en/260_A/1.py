def main():
    s = raw_input()
    if s[0] != s[1] and s[0] != s[2]:
        print s[0]
    elif s[1] != s[0] and s[1] != s[2]:
        print s[1]
    elif s[2] != s[0] and s[2] != s[1]:
        print s[2]
    else:
        print -1
