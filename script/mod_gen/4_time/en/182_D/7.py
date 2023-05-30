def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
        A[i] = ans
    print(max(A))
solve()
