def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        a[i] += l
    ans = 0
    for i in range(n):
        ans += a[i] * (n - i)
    for i in range(n):
        a[i] += r - l
    for i in range(n):
        ans = min(ans, a[i] * (n - i) + sum(a[i + 1:]))
    print(ans)

if __name__ == '__main__':
    main()