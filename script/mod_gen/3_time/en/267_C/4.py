def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n - m + 1)
    for i in range(n - m + 1):
        b[i] = sum(a[i:i+m])
    b.sort()
    ans = 0
    for i in range(m):
        ans += (i + 1) * b[n - m - i]
    print(ans)

if __name__ == '__main__':
    main()