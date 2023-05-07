def main():
    s = input()
    if len(s) == 1:
        if s == "R" or s == "U" or s == "D":
            print("Yes")
        else:
            print("No")
        return
    for i in range(1, len(s), 2):
        if s[i] == "R" or s[i] == "U" or s[i] == "D":
            continue
        else:
            print("No")
            return
    for i in range(0, len(s), 2):
        if s[i] == "L" or s[i] == "U" or s[i] == "D":
            continue
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()