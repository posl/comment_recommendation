def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 1 << 30
    j = 0
    for i in range(n):
        while j + 1 < m and B[j + 1] <= A[i]:
            j += 1
        ans = min(ans, abs(A[i] - B[j]))
        if j + 1 < m:
            ans = min(ans, abs(A[i] - B[j + 1]))
    print(ans)
solve()
