def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    b = [0] * (m + 1)
    for i in range(m):
        b[i + 1] = a[i] - a[i - 1] - 1
    b.sort()
    ans = 0
    for i in range(m - n + 1):
        ans += b[i]
    print(ans)

if __name__ == '__main__':
    main()