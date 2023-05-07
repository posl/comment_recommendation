def main():
    s = input()
    upper = False
    lower = False
    for i in range(len(s)):
        if s[i].isupper():
            upper = True
        if s[i].islower():
            lower = True
    if upper and lower and len(s) == len(set(s)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()