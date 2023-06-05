def main():
    n = int(input())
    a = list(map(int, input().split()))
    a += a
    s = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        s[i] = s[i - 1] + a[i - 1]
    ans = 0
    for i in range(n):
        ans = max(ans, s[i + n] - s[i] + min(a[i:i + n]))
    print(ans)

if __name__ == '__main__':
    main()