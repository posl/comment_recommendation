Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)

    ans = float('inf')
    for i in range(2**N):
        cost = 0
        alg = [0]*M
        for j in range(N):
            if i>>j & 1:
                cost += C[j]
                for k in range(M):
                    alg[k] += A[j][k]
        if all(a >= X for a in alg):
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

=======
Suggestion 2

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        cost = 0
        alg = [0]*M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    alg[k] += A[j][k]
        for k in range(M):
            if alg[k] < X:
                break
        else:
            ans = min(ans, cost)
    print(ans if ans != 10**9 else -1)

=======
Suggestion 3

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    min_cost = 10**6
    #bit全探索
    for i in range(2**N):
        #print(bin(i))
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        #print("cost = ", cost)
        #print("understand = ", understand)
        #print("min_cost = ", min_cost)
        if min_cost > cost and min(understand) >= X:
            min_cost = cost
    if min_cost == 10**6:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 4

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        C.append(tmp[0])
        A.append(tmp[1:])
    ans = 10**9
    for i in range(2**N):
        tmp = [0] * M
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]
        if min(tmp) >= X:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 5

def main():
    n,m,x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = -1
    for i in range(1 << n):
        cost = 0
        skill = [0] * m
        for j in range(n):
            if i >> j & 1:
                cost += c[j]
                for k in range(m):
                    skill[k] += a[j][k]
        if min(skill) >= x:
            if ans == -1:
                ans = cost
            else:
                ans = min(ans, cost)
    print(ans)

=======
Suggestion 6

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
    #print(N,M,X)
    min_cost = 1000000
    for i in range(2**N):
        #print(bin(i))
        cost = 0
        understand = [0]*M
        for j in range(N):
            if (i >> j) & 1 == 1:
                #print(j)
                cost += C[j]
                for k in range(M):
                    understand[k] += A[j][k]
        #print(cost)
        #print(understand)
        if min(understand) >= X:
            min_cost = min(min_cost,cost)
    if min_cost == 1000000:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 7

def main():
    N,M,X = map(int,input().split())
    C = []
    A = []
    for i in range(N):
        c,a = map(int,input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(2**N):
        cost = 0
        score = [0]*M
        for j in range(N):
            if (i>>j)%2 == 1:
                cost += C[j]
                for k in range(M):
                    score[k] += A[j][k]
        if min(score) >= X:
            ans = min(ans,cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def solve():
    N,M,X = map(int,input().split())
    C = []
    A = []
    for _ in range(N):
        c,a = map(int,input().split())
        C.append(c)
        A.append(a)
    #print(C)
    #print(A)
    ans = 10**10
    for i in range(1,2**N):
        cost = 0
        level = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        #print(level)
        if min(level) >= X:
            ans = min(ans,cost)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)

=======
Suggestion 9

def calc_cost(cost_list, book_list):
    total_cost = 0
    for i in range(len(book_list)):
        total_cost += cost_list[i] * book_list[i]
    return total_cost

=======
Suggestion 10

def calcCost(costs, algos):
    cost = 0
    for i in range(len(costs)):
        cost += costs[i] * algos[i]
    return cost
