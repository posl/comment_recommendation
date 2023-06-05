def main():
    N, M = map(int, input().split())
    A = [int(a) - 1 for a in input().split()]
    if M == 0:
        print(1)
        return
    A.sort()
    B = [0] * N
    for a in A:
        B[a] = 1
    C = [0] * N
    for i in range(N):
        C[i] = C[i - 1] + B[i]
    ans = N
    for i in range(M):
        l = 0
        r = N
        while l < r:
            m = (l + r) // 2
            if C[m] - C[A[i] - 1] == 0:
                r = m
            else:
                l = m + 1
        ans = min(ans, l - A[i])
    print(ans)
main()
