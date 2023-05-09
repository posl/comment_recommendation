def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()