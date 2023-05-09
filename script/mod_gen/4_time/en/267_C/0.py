def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    t = [0]
    for i in range(n):
        t.append(t[-1] + i * a[i])
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, t[i + m] - t[i] - s[i] * m)
    print(ans)

if __name__ == '__main__':
    main()