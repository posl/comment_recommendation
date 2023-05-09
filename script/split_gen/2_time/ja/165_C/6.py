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
