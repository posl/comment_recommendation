def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1 << 30
    for i in range(N):
        x = 0
        for j in range(i, N):
            x |= A[j]
            y = 0
            for k in range(j + 1, N):
                y ^= A[k]
                ans = min(ans, x | y)
    print(ans)
main()
