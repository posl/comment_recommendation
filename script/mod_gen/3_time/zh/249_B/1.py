def main():
    s = input()
    if s.islower():
        print("No")
        exit()
    if s.isupper():
        print("No")
        exit()
    if len(s) % 2 != 0:
        print("No")
        exit()
    if s[0] == s[1]:
        print("No")
        exit()
    if s[-1] == s[-2]:
        print("No")
        exit()
    print("Yes")

if __name__ == '__main__':
    main()