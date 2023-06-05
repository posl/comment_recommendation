def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * 41
    for i in range(n):
        for j in range(41):
            if a[i] >> j & 1:
                b[j] += 1
    ans = 0
    for i in range(40, -1, -1):
        if b[i] <= n // 2 and ans + (1 << i) <= k:
            ans += 1 << i
    s = 0
    for i in range(n):
        s += ans ^ a[i]
    print(s)

if __name__ == '__main__':
    main()