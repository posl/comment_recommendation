def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        exit()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            exit()
    print("Yes")
main()

if __name__ == '__main__':
    main()