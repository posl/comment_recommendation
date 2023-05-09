def main():
    s = input()
    if len(s) <= 1:
        print("No")
        return
    if not s[0].isupper():
        print("No")
        return
    if not s[-1].isupper():
        print("No")
        return
    for i in range(1,len(s)-1):
        if s[i].isupper():
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()