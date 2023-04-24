Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**10
    for i in range(2**N):
        cost = 0
        level = [0]*M
        for j in range(N):
            if (i>>j)&1 == 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all(x >= X for x in level):
            ans = min(ans, cost)
    if ans == 10**10:
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
    ans = float('inf')
    for i in range(2 ** N):
        cost = 0
        level = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all(x >= X for x in level):
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

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
    ans = 10**9
    for i in range(2**N):
        cost = 0
        level = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if all(x >= X for x in level):
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10**9
    for i in range(1<<N):
        cost = 0
        level = [0]*M
        for j in range(N):
            if (i>>j)&1:
                cost += C[j]
                for k in range(M):
                    level[k] += A[j][k]
        if min(level) >= X:
            ans = min(ans, cost)
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 5

def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    ans = 10000000000
    for i in range(2**N):
        sumA = [0] * M
        sumC = 0
        for j in range(N):
            if (i >> j) & 1:
                sumC += C[j]
                for k in range(M):
                    sumA[k] += A[j][k]
        if all(x >= X for x in sumA):
            ans = min(ans, sumC)
    if ans == 10000000000:
        print(-1)
    else:
        print(ans)

=======
Suggestion 6

def main():
    n, m, x = map(int, input().split())
    c = [0] * n
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        c[i], *a[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** n):
        cost = 0
        level = [0] * m
        for j in range(n):
            if i >> j & 1:
                cost += c[j]
                for k in range(m):
                    level[k] += a[j][k]
        if all(l >= x for l in level):
            ans = min(ans, cost)
    print(ans if ans < 10 ** 9 else -1)

=======
Suggestion 7

def main():
    n, m, x = map(int, input().split())
    c = [0] * n
    a = [[0] * m for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split()))
        c[i] = tmp[0]
        for j in range(m):
            a[i][j] = tmp[j + 1]

    ans = 10 ** 9
    for i in range(2 ** n):
        tmp = [0] * m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                cost += c[j]
                for k in range(m):
                    tmp[k] += a[j][k]
        if all([x <= t for t in tmp]):
            ans = min(ans, cost)

    if ans == 10 ** 9:
        print(-1)
    else:
        print(ans)

=======
Suggestion 8

def solve():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        l = list(map(int, input().split()))
        C.append(l[0])
        A.append(l[1:])
    ans = 10**9 + 1
    for i in range(2**N):
        S = [0] * M
        cost = 0
        for j in range(N):
            if (i >> j) & 1:
                cost += C[j]
                for k in range(M):
                    S[k] += A[j][k]
        if min(S) >= X:
            ans = min(ans, cost)
    if ans == 10**9 + 1:
        print(-1)
    else:
        print(ans)

=======
Suggestion 9

def solve():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**9+1
    for bit in range(1 << N):
        cost = 0
        level = [0] * M
        for i in range(N):
            if (bit >> i) & 1:
                cost += A[i][0]
                for j in range(M):
                    level[j] += A[i][j+1]
        if min(level) >= X:
            ans = min(ans, cost)
    if ans == 10**9+1:
        print(-1)
    else:
        print(ans)

=======
Suggestion 10

def  main():
     #Input
     N, M, X = map(int, input().split())
     C = []
     A = []
     for  i  in  range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
     #Process
     ans = 10 ** 10
     for  i  in  range(1 << N):
        cost = 0
        level = [0] * M
        for  j  in  range(N):
            if  i >> j & 1:
                cost += C[j]
                for  k  in  range(M):
                    level[k] += A[j][k]
         #Output
         if  min(level) >= X:
            ans = min(ans, cost)
     print( -1  if  ans == 10 ** 10  else  ans)
