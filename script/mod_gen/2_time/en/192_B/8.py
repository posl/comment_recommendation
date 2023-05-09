def main():
    s = input()
    if len(s) == 1:
        print("Yes")
        return
    elif len(s) == 2:
        if s[0].islower() and s[1].isupper():
            print("Yes")
            return
        else:
            print("No")
            return
    else:
        for i in range(0, len(s), 2):
            if s[i].isupper():
                print("No")
                return
        for i in range(1, len(s), 2):
            if s[i].islower():
                print("No")
                return
        print("Yes")
        return
main()

if __name__ == '__main__':
    main()