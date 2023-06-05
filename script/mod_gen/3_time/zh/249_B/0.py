def main():
    s = input()
    if s.islower() or s.isupper():
        print("No")
        return
    if s[0].islower() or s[-1].isupper():
        print("No")
        return
    for i in range(1, len(s) - 1):
        if s[i].isupper():
            if s[i + 1].isupper() or s[i - 1].isupper():
                print("No")
                return
        else:
            if s[i + 1].islower() or s[i - 1].islower():
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()