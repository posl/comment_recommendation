def main():
    s = input()
    t = 'atcoder'
    if s == t:
        print(0)
        return
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += len(s) - i - 1
            break
    for i in range(len(s)-1, -1, -1):
        if s[i] != t[i]:
            ans += i
            break
    print(ans)

if __name__ == '__main__':
    main()