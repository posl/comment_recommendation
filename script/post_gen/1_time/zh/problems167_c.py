Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,x=map(int,input().split())
    c,a=[],[]
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(c)
    print(a)

=======
Suggestion 2

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        C.append(list(map(int, input().split())))
    for i in range(N):
        A.append(C[i][1:])
        C[i] = C[i][0]

    min_cost = -1
    for i in range(2**N):
        cost = 0
        understand = [0 for i in range(M)]
        for j in range(N):
            if i & (1 << j):
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        if min(understand) >= X:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)

=======
Suggestion 3

def main():
    N,M,X = map(int,input().split())
    C = []
    A = []
    for i in range(N):
        C.append(list(map(int,input().split())))
        A.append(C[i][1:])
    #print(N,M,X)
    #print(C)
    #print(A)
    #print(len(C),len(A))
    #print(len(C[0]),len(A[0]))
    #print(len(C[1]),len(A[1]))
    #print(len(C[2]),len(A[2]))
    #print(len(C[3]),len(A[3]))
    #print(len(C[4]),len(A[4]))
    #print(len(C[5]),len(A[5]))
    #print(len(C[6]),len(A[6]))
    #print(len(C[7]),len(A[7]))
    #print(len(C[8]),len(A[8]))
    #print(len(C[9]),len(A[9]))
    #print(len(C[10]),len(A[10]))
    #print(len(C[11]),len(A[11]))
    #print(len(C[12]),len(A[12]))
    #print(len(C[13]),len(A[13]))
    #print(len(C[14]),len(A[14]))
    #print(len(C[15]),len(A[15]))
    #print(len(C[16]),len(A[16]))
    #print(len(C[17]),len(A[17]))
    #print(len(C[18]),len(A[18]))
    #print(len(C[19]),len(A[19]))
    #print(len(C[20]),len(A[20]))
    #print(len(C[21]),len(A[21]))
    #print(len(C[22]),len(A[22]))
    #print(len(C[23]),len(A[23]))
    #print(len(C[24]),len(A[24]))
    #print(len(C[25]),len(A[25]))
    #print(len(C[26]),len(A[26]))
    #print(len(C[27]),len(A[27]))
    #print(len(C[28]),len(A[28]))
    #print(len(C[29]),len(A[29]))
    #print(len(C[30]),len(A[30]))
    #print(len(C[31]),len(A[31]))
    #print(len(C[32]),len(A[32

=======
Suggestion 4

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c_a = list(map(int, input().split()))
        c.append(c_a[0])
        a.append(c_a[1:])
    print(c)
    print(a)

=======
Suggestion 5

def dp(N,M,X,C,A):
    dp = [[float('inf') for _ in range(X+1)] for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M-1,-1,-1):
            for k in range(X+1):
                if k >= C[i]:
                    dp[j+1][k] = min(dp[j+1][k],dp[j][k-C[i]]+A[i])
    return dp[M][X] if dp[M][X] != float('inf') else -1

=======
Suggestion 6

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    #print(C)
    #print(A)
    min_cost = 10 ** 6
    for i in range(2 ** N):
        cost = 0
        level = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all([l >= X for l in level]):
            min_cost = min(min_cost, cost)
    if min_cost == 10 ** 6:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 7

def get_min_cost(n, m, x, costs, understand):
    costs = [costs[i] for i in range(n) if understand[i] < x]
    if len(costs) == 0:
        return 0
    min_cost = min(costs)
    min_cost_index = costs.index(min_cost)
    understand = [understand[i] + understand[min_cost_index] for i in range(n)]
    return min_cost + get_min_cost(n, m, x, costs, understand)

n, m, x = map(int, input().split())
costs = []
understand = []
for i in range(n):
    cost, *understand_level = map(int, input().split())
    costs.append(cost)
    understand.append(sum(understand_level))
print(get_min_cost(n, m, x, costs, understand))

=======
Suggestion 8

def main():
    n, m, x = map(int, input().split())
    a = []
    c = []
    for i in range(n):
        c_i, *a_i = map(int, input().split())
        a.append(a_i)
        c.append(c_i)

    min_cost = 10 ** 9
    for i in range(1 << n):
        cost = 0
        understanding = [0] * m
        for j in range(n):
            if i >> j & 1:
                for k in range(m):
                    understanding[k] += a[j][k]
                cost += c[j]
        if all(x <= u for u in understanding):
            min_cost = min(min_cost, cost)
    print(min_cost if min_cost < 10 ** 9 else -1)

=======
Suggestion 9

def solve(n, m, x, c, a):
    ans = 10**10
    for i in range(2**n):
        cost = 0
        level = [0]*m
        for j in range(n):
            if ((i>>j)&1):
                cost += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, cost)
    if ans == 10**10:
        return -1
    else:
        return ans

n, m, x = map(int, input().split())
c = []
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    c.append(tmp[0])
    a.append(tmp[1:])
print(solve(n, m, x, c, a))

=======
Suggestion 10

def main():
    # 读取数据
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        temp = list(map(int, input().split()))
        C.append(temp[0])
        A.append(temp[1:])
    # print(N, M, X)
    # print(C)
    # print(A)
    # 算法
    # 1. 找到满足条件的组合，求出最小值
    # 2. 没有满足条件的组合，输出-1
    # 3. 有满足条件的组合，输出最小值
    # 4. 满足条件的组合，求出最小值
    # 5. 没有满足条件的组合，输出-1
    # 6. 有满足条件的组合，输出最小值
    # 7. 满足条件的组合，求出最小值
    # 8. 没有满足条件的组合，输出-1
    # 9. 有满足条件的组合，输出最小值
    # 10. 满足条件的组合，求出最小值
    # 11. 没有满足条件的组合，输出-1
    # 12. 有满足条件的组合，输出最小值
    # 13. 满足条件的组合，求出最小值
    # 14. 没有满足条件的组合，输出-1
    # 15. 有满足条件的组合，输出最小值
    # 16. 满足条件的组合，求出最小值
    # 17. 没有满足条件的组合，输出-1
    # 18. 有满足条件的组合，输出最小值
    # 19. 满足条件的组合，求出最小值
    # 20
