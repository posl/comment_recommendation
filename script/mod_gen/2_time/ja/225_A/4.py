def main():
    s = input()
    if len(s) == 3:
        if s[0] == s[1] == s[2]:
            print(1)
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print(3)
        else:
            print(6)
    else:
        print("length error")

if __name__ == '__main__':
    main()