def main():
    s = input()
    if len(s) == 1:
        print("Yes")
        return
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] == "L":
                print("No")
                return
        else:
            if s[i] == "R":
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()