Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N,M,X = map(int,input().split())
    C = []
    A = []
    for i in range(N):
        c,a = map(int,input().split())
        C.append(c)
        A.append(a)
    #print(C)
    #print(A)

    min_cost = 1000000000
    for i in range(2**N):
        cost = 0
        level = [0 for _ in range(M)]
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if min(level) >= X:
            min_cost = min(min_cost,cost)
    if min_cost == 1000000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 2

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(c)
    print(a)
    print(n,m,x)

=======
Suggestion 3

def dfs(i, cost, level):
    if i == n:
        if level >= x:
            return cost
        else:
            return -1
    else:
        return min(dfs(i+1, cost + c[i], [level[j] + a[i][j] for j in range(m)]), dfs(i+1, cost, level))

n, m, x = map(int, input().split())
c = [0]*n
a = [[0]*m for _ in range(n)]
for i in range(n):
    c[i], *a[i] = map(int, input().split())
print(dfs(0, 0, [0]*m))

=======
Suggestion 4

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
    c = [c[i][0] for i in range(n)]
    # print(n, m, x)
    # print(c)
    # print(a)
    # print()
    import itertools
    min_cost = 10**9
    for i in range(1, n+1):
        for j in itertools.combinations(range(n), i):
            # print(j)
            temp_cost = 0
            temp_a = [0]*m
            for k in j:
                temp_cost += c[k]
                for l in range(m):
                    temp_a[l] += a[k][l]
            # print(temp_cost)
            # print(temp_a)
            # print()
            if min(temp_a) >= x:
                min_cost = min(min_cost, temp_cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 5

def input():
    return list(map(int, input().split()))

=======
Suggestion 6

def main():
    # n,m,x = map(int,input().split())
    # c_a = []
    # for i in range(n):
    #     c_a.append(list(map(int,input().split())))
    n,m,x = 3,3,10
    c_a = [[60,2,2,4],[70,8,7,9],[50,2,3,9]]
    # n,m,x = 3,3,10
    # c_a = [[100,3,1,4],[100,1,5,9],[100,2,6,5]]
    # n,m,x = 8,5,22
    # c_a = [[100,3,7,5,3,1],[164,4,5,2,7,8],[334,7,2,7,2,9],[234,4,7,2,8,2],[541,5,4,3,3,6],[235,4,8,6,9,7],[394,3,6,1,6,2],[872,8,4,3,7,2]]
    min_price = 100000000
    for i in range(2**n):
        total_price = 0
        total_a = [0]*m
        for j in range(n):
            if i & (1<<j):
                total_price += c_a[j][0]
                for k in range(m):
                    total_a[k] += c_a[j][k+1]
        if min(total_a) >= x and total_price < min_price:
            min_price = total_price
    if min_price == 100000000:
        print(-1)
    else:
        print(min_price)

=======
Suggestion 7

def get_min_cost(N, M, X, C, A):
    min_cost = -1
    for i in range(1, 2 ** N):
        cost = 0
        algos = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    algos[k] += A[j][k]
        if min(algos) >= X:
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    return min_cost

=======
Suggestion 8

def dfs(n, m, x, c, a, i, money, sum):
    if i == n:
        if sum >= x:
            return money
        else:
            return -1

    money1 = dfs(n, m, x, c, a, i + 1, money, sum)
    money2 = dfs(n, m, x, c, a, i + 1, money + c[i], sum + a[i])
    if money1 == -1:
        return money2
    elif money2 == -1:
        return money1
    else:
        return min(money1, money2)

=======
Suggestion 9

def main():
    n,m,x = map(int,input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
    for i in range(n):
        a.append(c[i][1:])
    print(c)
    print(a)

main()
