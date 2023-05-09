def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 2 ** 30
    for i in range(1, 2 ** (N - 1)):
        x, y = 0, 0
        for j in range(N):
            y |= A[j]
            if (i >> j) & 1:
                x ^= y
                y = 0
        x ^= y
        ans = min(ans, x)
    print(ans)
main()
