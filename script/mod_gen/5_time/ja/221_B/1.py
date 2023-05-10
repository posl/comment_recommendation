def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s) - 1):
            if s[i] != t[i]:
                if s[i] != t[i + 1] or s[i + 1] != t[i]:
                    print("No")
                    exit()
        print("Yes")

if __name__ == '__main__':
    main()