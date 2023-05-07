def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if not s[i] in "RUD":
                print("No")
                return
        else:
            if not s[i] in "LUD":
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()