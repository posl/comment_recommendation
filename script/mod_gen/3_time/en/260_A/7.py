def main():
    # Read the string
    s = input()
    # If the string has only one character, print it
    if len(s) == 1:
        print(s)
    # If the string has two characters, print the one that is different
    elif len(s) == 2:
        if s[0] == s[1]:
            print(-1)
        else:
            print(s[0])
    # If the string has three characters, print the one that is different
    elif len(s) == 3:
        if s[0] == s[1] and s[0] == s[2]:
            print(-1)
        elif s[0] == s[1]:
            print(s[2])
        elif s[0] == s[2]:
            print(s[1])
        elif s[1] == s[2]:
            print(s[0])
    # If the string has more than three characters, print -1
    else:
        print(-1)

if __name__ == '__main__':
    main()