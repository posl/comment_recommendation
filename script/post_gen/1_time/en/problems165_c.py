Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1

    ans = 0
    for i in range(1, M + 1):
        ans = max(ans, dfs(1, [i], N, M, Q, a, b, c, d))

    print(ans)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    ans = 0
    for A in combinations_with_replacement(range(1, M + 1), N):
        score = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                score += d[i]
        ans = max(ans, score)
    print(ans)

=======
Suggestion 3

def solve():
    N, M, Q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    A = [0] * N
    ans = 0
    def dfs(i, A_i):
        if i == N:
            score = 0
            for j in range(Q):
                if A[b[j] - 1] - A[a[j] - 1] == c[j]:
                    score += d[j]
            global ans
            ans = max(ans, score)
            return
        for j in range(A_i, M + 1):
            A[i] = j
            dfs(i + 1, j)
    dfs(0, 1)
    print(ans)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N + 1)
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        A[a - 1] += d
        A[b] -= d
    for i in range(N):
        A[i + 1] += A[i]
    print(max(A))

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    A = [1] * N
    score = 0
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        if A[b-1] - A[a-1] == c:
            score += d
    print(score)

=======
Suggestion 6

def main():
    N, M, Q = [int(x) for x in input().split()]
    queries = []
    for _ in range(Q):
        queries.append([int(x) for x in input().split()])
    print(solve(N, M, Q, queries))

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N + 1)
    A[0] = 1
    A[N] = M
    score = 0
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        if A[b] - A[a] == c:
            score += d
    print(score)

=======
Suggestion 8

def main():
    N,M,Q=map(int,input().split())
    A=[0]*N
    A[0]=1
    A[N-1]=M
    ans=0
    for i in range(Q):
        a,b,c,d=map(int,input().split())
        if A[b-1]-A[a-1]==c:
            ans+=d
    print(ans)

=======
Suggestion 9

def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[N-1] = M
    score = [0]
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        score.append(d)
        A[a-1] = c + 1
        A[b-1] = M - c
    print(sum(score))
