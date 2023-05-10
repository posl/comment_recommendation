def main():
    n, c = map(int, input().split())
    s = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        s.append((a, c))
        s.append((b + 1, -c))
    s.sort()
    ans = 0
    t = 0
    for i in range(2 * n):
        if i > 0:
            ans += min(c, t) * (s[i][0] - s[i - 1][0])
        t += s[i][1]
    print(ans)

if __name__ == '__main__':
    main()