def solution():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            p = sum(A[:i])
            q = sum(A[i:j])
            r = sum(A[j:N])
            s = sum(A) - p - q - r
            ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)
solution()
