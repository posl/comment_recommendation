def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")
main()

if __name__ == '__main__':
    main()