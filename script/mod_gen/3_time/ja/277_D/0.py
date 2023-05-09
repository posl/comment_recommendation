def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    for i in range(n):
        ok = n + 1
        ng = i
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if s[mid] - s[i] >= m:
                ok = mid
            else:
                ng = mid
        ans = max(ans, s[ok] - s[i] - m)
    print(ans)

if __name__ == '__main__':
    main()