def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(-1)
    else:
        if s[0] != s[1] and s[0] != s[2]:
            print(s[0])
        elif s[1] != s[2]:
            print(s[1])
        else:
            print(s[2])
