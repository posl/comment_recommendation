def solve():
    N = int(input())
    X,Y = map(int,input().split())
    A = []
    B = []
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    dp = [[0]*(Y+1) for _ in range(X+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(X,-1,-1):
            for k in range(Y,-1,-1):
                if dp[j][k] == 1:
                    dp[min(j+A[i],X)][min(k+B[i],Y)] = 1
    ans = 0
    for i in range(1,N+1):
        if dp[X][Y] == 1:
            ans = i
            break
    print(ans if ans > 0 else -1)
solve()
