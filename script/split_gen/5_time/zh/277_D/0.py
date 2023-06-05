def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        if i == 0:
            B[i] = A[i]
        else:
            B[i] = (B[i - 1] + A[i]) % M
    ans = 0
    for i in range(N - 1):
        if B[i] <= B[i + 1]:
            ans += B[i + 1] - B[i]
        else:
            ans += B[i + 1] + M - B[i]
    print(ans)
