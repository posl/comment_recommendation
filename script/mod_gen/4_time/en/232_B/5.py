def main():
    s = input()
    t = input()
    for i in range(0, len(s)):
        if s == t:
            print("Yes")
            return
        else:
            s = s[-1] + s[:-1]
    print("No")
main()

if __name__ == '__main__':
    main()