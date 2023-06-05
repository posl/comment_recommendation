def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        for i in range(len(s)):
            if s == t:
                print("Yes")
                break
            else:
                s = s[1:] + s[0]
        else:
            print("No")

if __name__ == '__main__':
    main()