def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if K > 0:
            if A[i] - X > 0:
                ans += X
                K -= 1
            else:
                ans += A[i]
        else:
            ans += A[i]
    print(ans)
