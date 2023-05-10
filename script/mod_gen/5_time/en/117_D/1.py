def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(50, -1, -1):
        c = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                c += 1
        if c <= n / 2 and ans + (1 << i) <= k:
            ans += (1 << i)
    f = 0
    for i in range(n):
        f += ans ^ a[i]
    print(f)

if __name__ == '__main__':
    main()