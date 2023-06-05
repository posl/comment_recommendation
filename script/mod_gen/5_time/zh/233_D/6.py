def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 0
    j = 0
    for i in range(n):
        while j <= n and s[j] - s[i] < k:
            j += 1
        if s[j] - s[i] == k:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()