def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = float('inf')
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            x = s[i]
            y = s[j] - s[i]
            z = s[n] - s[j]
            ans = min(ans, max(x, y, z) - min(x, y, z))
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

if __name__ == '__main__':
    main()