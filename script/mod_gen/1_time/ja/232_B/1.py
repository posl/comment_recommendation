def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if (ord(t[i]) - ord(s[i]) + 26) % 26 != 0:
            print("No")
            exit()
    print("Yes")
    return
main()

if __name__ == '__main__':
    main()