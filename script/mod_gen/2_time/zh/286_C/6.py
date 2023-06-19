def main():
    n, a, b = map(int, input().split())
    s = input()
    s = list(s)
    s.reverse()
    ans = 0
    for i in range(n):
        if s[i] == s[n-1-i]:
            continue
        elif s[i] == 'a':
            ans += a
        else:
            ans += b
    print(ans)

if __name__ == '__main__':
    main()