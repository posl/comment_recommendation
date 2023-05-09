def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print(1)
    elif s[0] != s[1] and s[1] != s[2] and s[0] != s[2]:
        print(6)
    else:
        print(3)

if __name__ == '__main__':
    main()