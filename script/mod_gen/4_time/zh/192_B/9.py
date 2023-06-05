def main():
    s = input()
    if len(s) == 1:
        if s.islower():
            print("Yes")
        else:
            print("No")
    else:
        for i in range(1, len(s), 2):
            if s[i].isupper():
                print("No")
                return
        for i in range(0, len(s), 2):
            if s[i].islower():
                print("No")
                return
        print("Yes")

if __name__ == '__main__':
    main()