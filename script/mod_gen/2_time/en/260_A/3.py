def main():
    s = input()
    if len(s) == 3:
        if s[0] == s[1] and s[0] == s[2]:
            print(-1)
        elif s[0] == s[1]:
            print(s[2])
        elif s[0] == s[2]:
            print(s[1])
        elif s[1] == s[2]:
            print(s[0])
        else:
            print(s[0])
    else:
        print('Input must be a string of length 3')

if __name__ == '__main__':
    main()