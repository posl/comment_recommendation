def main():
    s = input()
    for i in range(len(s)):
        if (i+1)%2 == 1:
            if s[i] == "R" or s[i] == "U" or s[i] == "D":
                continue
            else:
                print("No")
                return
        else:
            if s[i] == "L" or s[i] == "U" or s[i] == "D":
                continue
            else:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()