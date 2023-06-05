def main():
    s = input()
    t = input()
    if (len(s) != len(t)):
        print("No")
        return
    for i in range(len(s)):
        if (s[i] != t[i]):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()