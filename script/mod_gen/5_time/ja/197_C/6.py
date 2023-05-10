def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2**30
    for i in range(2**(N-1)):
        ors = 0
        xors = 0
        for j in range(N):
            ors |= A[j]
            if (i >> j) & 1 == 1:
                xors ^= ors
                ors = 0
        xors ^= ors
        ans = min(ans, xors)
    print(ans)

if __name__ == '__main__':
    main()