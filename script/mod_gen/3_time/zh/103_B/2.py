def main():
    s = input()
    t = input()
    if len(s) == len(t):
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                print("Yes")
                exit()
        print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()