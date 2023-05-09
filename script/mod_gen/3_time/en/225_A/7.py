def main():
    s = input()
    n = len(s)
    if n == 2:
        if s[0] == s[1]:
            print(1)
        else:
            print(2)
    else:
        if s[0] == s[1] and s[1] == s[2]:
            print(1)
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print(3)
        else:
            print(6)

if __name__ == '__main__':
    main()