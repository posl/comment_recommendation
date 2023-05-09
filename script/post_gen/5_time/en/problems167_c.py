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
    # print(N, M, X, C, A)

    min_cost = 10 ** 10
    for i in range(2 ** N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if min(understanding) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10 ** 10:
        print(-1)
    else:
        print(min_cost)

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
    min_cost = -1
    for i in range(2**N):
        cost = 0
        understanding = [0]*M
        for j in range(N):
            if i & (1 << j):
                cost += C[j]
                understanding = [understanding[k] + A[j][k] for k in range(M)]
        if all([understanding[k] >= X for k in range(M)]):
            if min_cost == -1 or cost < min_cost:
                min_cost = cost
    print(min_cost)

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
    min_cost = 10**9
    for i in range(2**N):
        sum_cost = 0
        sum_A = [0]*M
        for j in range(N):
            if i>>j & 1:
                sum_cost += C[j]
                for k in range(M):
                    sum_A[k] += A[j][k]
        if all([a>=X for a in sum_A]):
            min_cost = min(min_cost, sum_cost)
    if min_cost == 10**9:
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
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    result = 10**6
    for i in range(2**N):
        cost = 0
        understanding = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if all([x>=X for x in understanding]):
            result = min(result, cost)
    if result == 10**6:
        print(-1)
    else:
        print(result)

=======
Suggestion 5

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
        tmp = [0]*M
        cost = 0
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    tmp[k] += A[j][k]
        if min(tmp) >= X:
            ans = min(ans, cost)
    if ans == 10**9:
        ans = -1
    print(ans)
main()

=======
Suggestion 6

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        c.append(tmp[0])
        a.append(tmp[1:])
    ans = 10 ** 9
    for i in range(2 ** n):
        tmp = 0
        tmp_a = [0] * m
        for j in range(n):
            if ((i >> j) & 1):
                tmp += c[j]
                for k in range(m):
                    tmp_a[k] += a[j][k]
        if all(x <= tmp_a[k] for k in range(m)):
            ans = min(ans, tmp)
    if ans == 10 ** 9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 7

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        x = list(map(int, input().split()))
        C.append(x[0])
        A.append(x[1:])
    min_cost = 10**9
    for i in range(2**N):
        cost = 0
        understanding_level = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    understanding_level[k] += A[j][k]
        if min(understanding_level) >= X:
            min_cost = min(min_cost, cost)
    if min_cost == 10**9:
        print(-1)
    else:
        print(min_cost)

=======
Suggestion 8

def main():
    n, m, x = map(int, input().split())
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int, input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]

    ans = 10**9

    for i in range(1 << n):
        cost = 0
        level = [0] * m
        for j in range(n):
            if i >> j & 1:
                cost += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if min(level) >= x:
            ans = min(ans, cost)

    if ans == 10**9:
        print(-1)
    else:
        print(ans)

main()

=======
Suggestion 9

def main():
    N, M, X = [int(i) for i in input().split()]
    A = []
    for i in range(N):
        A.append([int(i) for i in input().split()])
    min_cost = -1
    for i in range(2**N):
        cost = 0
        understanding = [0 for _ in range(M)]
        for j in range(N):
            if i & 2**j:
                cost += A[j][0]
                for k in range(M):
                    understanding[k] += A[j][k+1]
        if min_cost == -1 or (min_cost > cost and min(understanding) >= X):
            min_cost = cost
    print(min_cost)

=======
Suggestion 10

def check(x):
    sum = 0
    for i in range(0, N):
        sum += C[i] * (A[i][j] for j in range(0, M) if x & (1 << j) > 0)
    if sum >= X:
        return True
    else:
        return False
