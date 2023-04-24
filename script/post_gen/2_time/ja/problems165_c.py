Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(A):
    global ans
    if len(A) == N:
        score = 0
        for i in range(Q):
            if A[b[i]-1] - A[a[i]-1] == c[i]:
                score += d[i]
        ans = max(ans, score)
        return

    for i in range(A[-1], M+1):
        dfs(A+[i])

N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for _ in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

ans = 0
for i in range(1, M+1):
    dfs([i])
print(ans)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    query = []
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        query.append((a, b, c, d))
    ans = 0
    for A in range(1, M+1):
        for B in range(A, M+1):
            for C in range(B, M+1):
                for D in range(C, M+1):
                    for E in range(D, M+1):
                        for F in range(E, M+1):
                            for G in range(F, M+1):
                                for H in range(G, M+1):
                                    for I in range(H, M+1):
                                        for J in range(I, M+1):
                                            score = 0
                                            for a, b, c, d in query:
                                                if A <= a and b <= B:
                                                    score += c
                                                if C <= a and b <= D:
                                                    score += c
                                                if E <= a and b <= F:
                                                    score += c
                                                if G <= a and b <= H:
                                                    score += c
                                                if I <= a and b <= J:
                                                    score += c
                                            ans = max(ans, score)
    print(ans)

main()

=======
Suggestion 3

def dfs(A):
    global ans
    if len(A) == N:
        tmp = 0
        for a, b, c, d in Q:
            if A[b-1] - A[a-1] == c:
                tmp += d
        ans = max(ans, tmp)
        return
    for i in range(A[-1], M+1):
        dfs(A+[i])

N, M, Q = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
for i in range(1, M+1):
    dfs([i])
print(ans)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    query = [list(map(int, input().split())) for i in range(Q)]

    def dfs(A):
        if len(A) == N:
            score = 0
            for a, b, c, d in query:
                if A[b-1] - A[a-1] == c:
                    score += d
            return score
        else:
            for i in range(A[-1], M+1):
                A.append(i)
                yield from dfs(A)
                A.pop()

    ans = 0
    for i in range(1, M+1):
        ans = max(ans, max(dfs([i])))
    print(ans)

=======
Suggestion 5

def calc_score(A, N, Q, query):
    score = 0
    for i in range(Q):
        a = query[i][0]
        b = query[i][1]
        c = query[i][2]
        d = query[i][3]
        if A[b-1] - A[a-1] == c:
            score += d
    return score

=======
Suggestion 6

def calc_score(A, N, Q, query):
    score = 0
    for i in range(Q):
        a = query[i][0] - 1
        b = query[i][1] - 1
        c = query[i][2]
        d = query[i][3]
        if (A[b] - A[a]) == c:
            score += d
    return score

=======
Suggestion 7

def dfs(A, N, M, Q, a, b, c, d, score):
    if len(A) == N:
        global max_score
        max_score = max(score, max_score)
        return
    else:
        for i in range(A[-1], M+1):
            A.append(i)
            for j in range(Q):
                if A[b[j]-1] - A[a[j]-1] == c[j]:
                    score += d[j]
            dfs(A, N, M, Q, a, b, c, d, score)
            A.pop()
            for j in range(Q):
                if A[b[j]-1] - A[a[j]-1] == c[j]:
                    score -= d[j]

N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    a_, b_, c_, d_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)
    d.append(d_)
max_score = 0
for i in range(1, M+1):
    A = [i]
    score = 0
    dfs(A, N, M, Q, a, b, c, d, score)
print(max_score)

=======
Suggestion 8

def score_calc(a, b, c, d):
    score = 0
    for i in range(Q):
        if a[i] < b[i]:
            score += d[i]
    return score

=======
Suggestion 9

def get_max_score(n, m, q, abcd):
    def dfs(a, start):
        if len(a) == n:
            score = 0
            for b, c, d in abcd:
                if a[b-1] - a[a-1] == c:
                    score += d
            return score
        else:
            ans = 0
            for i in range(start, m+1):
                ans = max(ans, dfs(a + [i], i))
            return ans
    return dfs([], 1)

n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
print(get_max_score(n, m, q, abcd))

=======
Suggestion 10

def dfs(a, b, c, d, n, m, q, A, ans):
    if len(A) == n:
        if ans[0] < sum(d[i] for i in range(q) if A[b[i] - 1] - A[a[i] - 1] == c[i]):
            ans[0] = sum(d[i] for i in range(q) if A[b[i] - 1] - A[a[i] - 1] == c[i])
    else:
        for v in range(a[len(A) - 1], m + 1):
            A.append(v)
            dfs(a, b, c, d, n, m, q, A, ans)
            A.pop()

n, m, q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(q):
    a_, b_, c_, d_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)
    d.append(d_)

ans = [0]
for v in range(1, m + 1):
    dfs(a, b, c, d, n, m, q, [v], ans)

print(ans[0])
