def main():
    s = input()
    if len(s) % 2 == 1:
        print("No")
    else:
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "L":
                print("No")
                return
            elif i % 2 == 1 and s[i] == "R":
                print("No")
                return
        print("Yes")

if __name__ == '__main__':
    main()