Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, q = map(int, input().split())
    a = [0] * q
    b = [0] * q
    c = [0] * q
    d = [0] * q
    for i in range(q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1

    ans = 0
    A = [0] * n
    def dfs(i, A):
        nonlocal ans
        if i == n:
            now = 0
            for j in range(q):
                if A[b[j]] - A[a[j]] == c[j]:
                    now += d[j]
            ans = max(ans, now)
            return
        A[i] = A[i-1]
        while A[i] <= m:
            dfs(i+1, A)
            A[i] += 1
    dfs(0, A)
    print(ans)

=======
Suggestion 2

def dfs(A):
    if len(A) == N:
        score = 0
        for a, b, c, d in Q:
            if A[b-1] - A[a-1] == c:
                score += d
        return score
    else:
        last = A[-1]
        ans = 0
        for i in range(last, M+1):
            A.append(i)
            ans = max(ans, dfs(A))
            A.pop()
        return ans

N, M, Q = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(Q)]
ans = dfs([1])
print(ans)

=======
Suggestion 3

def calc_score(a, b, c, d, A):
    score = 0
    for i in range(len(a)):
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            score += d[i]
    return score

=======
Suggestion 4

def score(a):
    ans = 0
    for i in range(Q):
        if a[b[i]-1] - a[a[i]-1] == c[i]:
            ans += d[i]
    return ans

=======
Suggestion 5

def dfs(A,N,M,Q):
    global ans
    if len(A) == N:
        score = 0
        for i in range(Q):
            if A[b[i]-1]-A[a[i]-1] == c[i]:
                score += d[i]
        ans = max(ans,score)
        return
    A.append(A[-1])
    while A[-1] <= M:
        dfs(A,N,M,Q)
        A[-1] += 1
    A.pop()
    return

N,M,Q = map(int,input().split())
a,b,c,d = [],[],[],[]
for i in range(Q):
    A,B,C,D = map(int,input().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)
ans = 0
dfs([1],N,M,Q)
print(ans)

=======
Suggestion 6

def calc_score(arr, N, Q):
    score = 0
    for i in range(Q):
        a = arr[i][0]
        b = arr[i][1]
        c = arr[i][2]
        d = arr[i][3]
        if arr[b-1] - arr[a-1] == c:
            score += d
    return score

=======
Suggestion 7

def dfs(A, N, M, Q, abcd, ans):
    if len(A) == N:
        sum = 0
        for i in range(Q):
            if A[abcd[i][1]-1] - A[abcd[i][0]-1] == abcd[i][2]:
                sum += abcd[i][3]
        ans[0] = max(ans[0], sum)
        return

    for i in range(A[-1], M+1):
        A.append(i)
        dfs(A, N, M, Q, abcd, ans)
        A.pop()

=======
Suggestion 8

def dfs(A, N, M, Q, a, b, c, d):
    if len(A) == N:
        #print(A)
        return calc(A, Q, a, b, c, d)
    else:
        for i in range(A[-1], M+1):
            dfs(A+[i], N, M, Q, a, b, c, d)

=======
Suggestion 9

def main():
    N, M, Q = map(int, input().split())

    A = [1] * N
    for i in range(N):
        A[i] = 1

    max = 0
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        if A[b-1] - A[a-1] == c:
            A[b-1] = d
            if max < sum(A):
                max = sum(A)

    print(max)

=======
Suggestion 10

def dfs(A, N, M, Q, query, start, end, score):
    if len(A) == N:
        score = max(score, calc_score(A, query))
        return score
    for i in range(start, end + 1):
        A.append(i)
        score = dfs(A, N, M, Q, query, i, end, score)
        A.pop()
    return score
