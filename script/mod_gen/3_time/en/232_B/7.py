def main():
    s = input().rstrip()
    t = input().rstrip()
    if s == t:
        print("Yes")
        return
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()