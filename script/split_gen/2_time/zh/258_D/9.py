def solve():
    N,X = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    ans += min(B)
    for i in range(N):
        ans += (X-1)*min(A[i],B[i])
    return ans
print(solve())
