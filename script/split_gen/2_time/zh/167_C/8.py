def solve():
    #读取输入
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    #枚举所有购买方案
    ans = float('inf')
    for i in range(2**N):
        cost = 0
        understand = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            ans = min(ans, cost)
    #输出
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
