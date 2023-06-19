def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print(0)
    elif s[0] == s[1] or s[1] == s[2]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()