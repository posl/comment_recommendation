def main():
    s = input()
    isHard = True
    for i in range(0, len(s)):
        if i % 2 == 0 and s[i].islower():
            isHard = False
        if i % 2 == 1 and s[i].isupper():
            isHard = False
    if isHard:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()