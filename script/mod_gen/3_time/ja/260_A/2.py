def main():
    s = input()
    if s[0] == s[1] and s[1] != s[2]:
        print(s[2])
    elif s[0] == s[2] and s[1] != s[2]:
        print(s[1])
    elif s[1] == s[2] and s[0] != s[2]:
        print(s[0])
    else:
        print(-1)

if __name__ == '__main__':
    main()