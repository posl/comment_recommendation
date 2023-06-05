def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                print("No")
                return
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()