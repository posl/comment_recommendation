def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a[:m])
    ans = s
    for i in range(1, n - m + 1):
        s += a[m + i - 1] - a[i - 1]
        ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()