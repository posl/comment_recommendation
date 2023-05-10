def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 2**30
    for i in range(2**n):
        ors = 0
        xors = 0
        for j in range(n):
            ors |= a[j]
            if i & 1<<j:
                xors ^= ors
                ors = 0
        xors ^= ors
        ans = min(ans, xors)
    print(ans)

if __name__ == '__main__':
    main()