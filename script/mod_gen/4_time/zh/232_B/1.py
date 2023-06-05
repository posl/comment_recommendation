def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        if s == t:
            print("Yes")
        else:
            for i in range(1, len(s)):
                if s[i:] + s[:i] == t:
                    print("Yes")
                    break
            else:
                print("No")

if __name__ == '__main__':
    main()