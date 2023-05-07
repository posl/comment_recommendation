def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, s[i + m] - s[i] + m * max(a[i:i + m]))
    print(ans)

if __name__ == '__main__':
    main()