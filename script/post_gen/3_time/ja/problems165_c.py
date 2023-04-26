Synthesizing 10/10 solutions

=======
Suggestion 1

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
    for i in range(1, M + 1):
        A = [i]
        for j in range(1, N):
            A.append(A[j - 1] + 1)
        score = 0
        for k in range(Q):
            if A[b[k] - 1] - A[a[k] - 1] == c[k]:
                score += d[k]
        ans = max(ans, score)
    print(ans)

=======
Suggestion 2

def solve():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
    ans = 0
    def dfs(A):
        global ans
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                    score += d[i]
            ans = max(ans, score)
            return
        if len(A) == 0:
            for i in range(1, M + 1):
                A.append(i)
                dfs(A)
                A.pop()
        else:
            for i in range(A[-1], M + 1):
                A.append(i)
                dfs(A)
                A.pop()
    dfs([])
    print(ans)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    A = [0] * Q
    B = [0] * Q
    C = [0] * Q
    D = [0] * Q
    for i in range(Q):
        A[i], B[i], C[i], D[i] = map(int, input().split())
    ans = 0
    for i in range(1, M + 1):
        A = [i]
        for j in range(2, N + 1):
            for k in range(A[j - 2], M + 1):
                A.append(k)
                for l in range(Q):
                    if A[B[l] - 1] - A[A[l] - 1] == C[l]:
                        ans += D[l]
    print(ans)

=======
Suggestion 4

def calc_score(A, Q, a, b, c, d):
    score = 0
    for i in range(Q):
        if A[b[i] - 1] - A[a[i] - 1] == c[i]:
            score += d[i]
    return score

=======
Suggestion 5

def dfs(A, N, M, Q, a, b, c, d, ans):
    if len(A) == N:
        tmp = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                tmp += d[i]
        ans = max(ans, tmp)
        return ans
    if len(A) == 0:
        A.append(1)
    else:
        A.append(A[-1])
    while A[-1] <= M:
        ans = dfs(A, N, M, Q, a, b, c, d, ans)
        A[-1] += 1
    A.pop()
    return ans

N, M, Q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(Q):
    tmp = list(map(int, input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
    c.append(tmp[2])
    d.append(tmp[3])
ans = 0
A = []
print(dfs(A, N, M, Q, a, b, c, d, ans))

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    ans = 0
    def dfs(A):
        global ans
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[query[i][1] - 1] - A[query[i][0] - 1] == query[i][2]:
                    score += query[i][3]
            ans = max(ans, score)
            return
        for i in range(A[-1], M + 1):
            dfs(A + [i])
    dfs([1])
    print(ans)

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    for A in dfs(N, M):
        score = 0
        for a, b, c, d in query:
            if A[b-1] - A[a-1] == c:
                score += d
        ans = max(ans, score)
    print(ans)

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())
    # N, M, Q = 10, 10, 1
    # a, b, c, d = 1, 10, 9, 1
    a, b, c, d = [0]*Q, [0]*Q, [0]*Q, [0]*Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        # a[i], b[i], c[i], d[i] = 1, 10, 9, 1
    ans = 0
    # A = [0]*N
    A = [0]*N
    def dfs(i):
        global ans
        if i == N:
            score = 0
            for j in range(Q):
                if A[b[j]-1] - A[a[j]-1] == c[j]:
                    score += d[j]
            ans = max(ans, score)
            return
        for j in range(1, M+1):
            A[i] = j
            dfs(i+1)
    dfs(0)
    print(ans)

=======
Suggestion 9

def solve():
    N, M, Q = map(int, input().split())
    A = [0 for i in range(N)]
    ans = 0
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        for j in range(a-1, b):
            A[j] = c
        score = 0
        for j in range(N-1):
            if A[j+1] - A[j] == d:
                score += d
        ans = max(ans, score)
    print(ans)

=======
Suggestion 10

def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]

    def dfs(A):
        # すべての数列を作る
        if len(A) == N:
            score = 0
            for a, b, c, d in ABCD:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            return score

        # すべての数列を作る
        res = 0
        for i in range(1, M + 1):
            if len(A) == 0 or A[-1] <= i:
                res = max(res, dfs(A + [i]))
        return res

    print(dfs([]))
