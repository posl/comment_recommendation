def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    f = [0] * 41
    for i in range(41):
        for j in range(n):
            if a[j] & (1 << i):
                f[i] += 1
    ans = 0
    for i in range(40, -1, -1):
        if ans + (1 << i) <= k:
            ans += (1 << i) * max(f[i], n - f[i])
        else:
            ans += (1 << i) * f[i]
    print(ans)

if __name__ == '__main__':
    main()