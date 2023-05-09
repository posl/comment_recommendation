def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1e9
    for i in range(1 << (n-1)):
        ors = 0
        xors = 0
        for j in range(n):
            ors |= a[j]
            if i >> j & 1:
                xors ^= ors
                ors = 0
        xors ^= ors
        ans = min(ans, xors)
    print(ans)

if __name__ == '__main__':
    main()