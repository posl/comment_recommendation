def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 10 ** 9
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            ans = min(ans, max(s[i], s[j] - s[i], s[n] - s[j]) - min(s[i], s[j] - s[i], s[n] - s[j]))
    print(ans)

if __name__ == '__main__':
    main()