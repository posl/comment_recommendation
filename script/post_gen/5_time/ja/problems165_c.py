Synthesizing 10/10 solutions

=======
Suggestion 1

def score(A, N, Q, a, b, c, d):
    ans = 0
    for i in range(Q):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            ans += d[i]
    return ans

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]

    ans = 0
    A = []
    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
            return
        for i in range(A[-1] if A else 1, M+1):
            A.append(i)
            dfs(A)
            A.pop()
    dfs(A)
    print(ans)

=======
Suggestion 3

def dfs(a):
    if len(a) == N:
        score = 0
        for i in range(Q):
            if a[b[i]-1] - a[a[i]-1] == c[i]:
                score += d[i]
        return score
    else:
        a.append(a[-1])
        while a[-1] <= M:
            dfs(a)
            a[-1] += 1
        a.pop()

N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
print(dfs([1]))

=======
Suggestion 4

def dfs(A, N, M, Q, a, b, c, d, ans):
    if len(A) == N:
        tmp = 0
        for i in range(Q):
            if A[b[i]-1] - A[a[i]-1] == c[i]:
                tmp += d[i]
        ans[0] = max(ans[0], tmp)
        return
    A.append(A[-1])
    while A[-1] <= M:
        dfs(A, N, M, Q, a, b, c, d, ans)
        A[-1] += 1
    A.pop()

N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

ans = [0]
A = [1]
dfs(A, N, M, Q, a, b, c, d, ans)
print(ans[0])

=======
Suggestion 5

def calc_score(A, N, Q, query):
    score = 0
    for q in query:
        if A[q[1]-1] - A[q[0]-1] == q[2]:
            score += q[3]
    return score

=======
Suggestion 6

def dfs(A, N, M, Q, a, b, c, d, ans):
    if len(A) == N:
        score = 0
        for i in range(Q):
            if A[b[i]-1] - A[a[i]-1] == c[i]:
                score += d[i]
        ans[0] = max(ans[0], score)
        return

    for i in range(A[-1], M+1):
        A.append(i)
        dfs(A, N, M, Q, a, b, c, d, ans)
        A.pop()

N, M, Q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

ans = [0]
for i in range(1, M+1):
    dfs([i], N, M, Q, a, b, c, d, ans)

print(ans[0])

=======
Suggestion 7

def dfs(A, count, N, M, Q, ans, abcd):
    if count == N:
        ans = max(ans, sum(abcd[i][3] for i in range(Q) if A[abcd[i][1]-1]-A[abcd[i][0]-1]==abcd[i][2]))
        return ans
    for i in range(A[-1], M+1):
        A.append(i)
        ans = dfs(A, count+1, N, M, Q, ans, abcd)
        A.pop()
    return ans

=======
Suggestion 8

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]

    # print(n, m, q)
    # print(abcd)

    A = [1] * n
    # print(A)
    ans = 0
    while True:
        # print(A)
        tmp = 0
        for a, b, c, d in abcd:
            if A[b-1] - A[a-1] == c:
                tmp += d
        ans = max(ans, tmp)

        A[0] += 1
        if A[0] > m:
            for i in range(1, n):
                if A[i-1] < m:
                    A[i-1] += 1
                    for j in range(i-1):
                        A[j] = A[i-1]
                    break
            else:
                break

    print(ans)

=======
Suggestion 9

def get_max_score(N,M,Q,query):
    ans = 0
    A = [1]*N
    while A[0] <= M:
        score = 0
        for i in range(Q):
            if A[query[i][1]-1] - A[query[i][0]-1] == query[i][2]:
                score += query[i][3]
        if score > ans:
            ans = score
        A[-1] += 1
        for i in range(N-1,0,-1):
            if A[i] > M:
                A[i] = 1
                A[i-1] += 1
    return ans

=======
Suggestion 10

def calc_score(A,B):
    score = 0
    for i in range(Q):
        if A[B[i][1]-1] - A[B[i][0]-1] == B[i][2]:
            score += B[i][3]
    return score
