def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    if len(s) != len(t):
        print(-1)
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print(i)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()