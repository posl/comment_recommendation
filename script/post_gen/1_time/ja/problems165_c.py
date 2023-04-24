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
    ans = 0
    def dfs(A):
        if len(A) == n:
            s = 0
            for i in range(q):
                if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                    s += d[i]
            nonlocal ans
            ans = max(ans, s)
            return
        if len(A) == 0:
            for i in range(1, m + 1):
                A.append(i)
                dfs(A)
                A.pop()
        else:
            for i in range(A[-1], m + 1):
                A.append(i)
                dfs(A)
                A.pop()
    dfs([])
    print(ans)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    a, b, c, d = [], [], [], []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    ans = 0
    for i in range(M):
        A = [i+1]
        for j in range(1, N):
            A.append(A[j-1]+1)
        for j in range(Q):
            if A[b[j]-1]-A[a[j]-1] == c[j]:
                ans += d[j]
    print(ans)

=======
Suggestion 3

def main():
    n,m,q = map(int,input().split())
    a = [0] * q
    b = [0] * q
    c = [0] * q
    d = [0] * q
    for i in range(q):
        a[i],b[i],c[i],d[i] = map(int,input().split())
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == n:
            score = 0
            for i in range(q):
                if A[b[i]-1] - A[a[i]-1] == c[i]:
                    score += d[i]
            ans = max(ans,score)
            return
        A.append(A[-1])
        while A[-1] <= m:
            dfs(A)
            A[-1] += 1
        A.pop()
    dfs([1])
    print(ans)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for i in range(Q)]

    def dfs(A):
        if len(A) == N:
            score = 0
            for i in range(Q):
                if A[abcd[i][1]-1] - A[abcd[i][0]-1] == abcd[i][2]:
                    score += abcd[i][3]
            return score
        else:
            score = 0
            for i in range(A[-1], M+1):
                score = max(score, dfs(A+[i]))
            return score

    print(dfs([1]))

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]
    A = [1]*N
    ans = 0
    def dfs(i):
        nonlocal ans
        if i == N:
            score = 0
            for j in range(Q):
                if A[ABCD[j][1]-1] - A[ABCD[j][0]-1] == ABCD[j][2]:
                    score += ABCD[j][3]
            ans = max(ans, score)
            return
        for j in range(A[i-1], M+1):
            A[i] = j
            dfs(i+1)
    dfs(1)
    print(ans)

=======
Suggestion 6

def dfs(a, i, n, m, q, abcd):
    if i == n:
        score = 0
        for j in range(q):
            if a[abcd[j][1] - 1] - a[abcd[j][0] - 1] == abcd[j][2]:
                score += abcd[j][3]
        return score

    ans = 0
    for j in range(a[i - 1], m + 1):
        a[i] = j
        ans = max(ans, dfs(a, i + 1, n, m, q, abcd))
    return ans

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[-1] = M
    ans = 0
    for i in range(1, N-1):
        A[i] = i + 1

    def dfs(A, i):
        global ans
        if i == N:
            score = 0
            for j in range(Q):
                a, b, c, d = map(int, input().split())
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
            return
        for j in range(A[i-1], M+1):
            A[i] = j
            dfs(A, i+1)
    dfs(A, 1)
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    #初期値
    A = [1]*N
    ans = 0
    #dfs
    def dfs(A, index):
        global ans
        if index == N:
            #得点計算
            score = 0
            for i in range(Q):
                if A[abcd[i][1]-1] - A[abcd[i][0]-1] == abcd[i][2]:
                    score += abcd[i][3]
            ans = max(ans, score)
            return
        for i in range(A[index-1], M+1):
            A[index] = i
            dfs(A, index+1)
    dfs(A, 1)
    print(ans)

=======
Suggestion 9

def dfs(a, n, m, q, a_i, b_i, c_i, d_i):
    if len(a) == n:
        return score(a, q, a_i, b_i, c_i, d_i)
    if len(a) == 0:
        num = 1
    else:
        num = a[-1]
    ans = 0
    while num <= m:
        a.append(num)
        ans = max(ans, dfs(a, n, m, q, a_i, b_i, c_i, d_i))
        a.pop()
        num += 1
    return ans

=======
Suggestion 10

def dfs(A, M, Q, abcd, index=0, score=0):
    if index == len(A):
        return score
    else:
        max_score = 0
        for i in range(A[index-1], M+1):
            A[index] = i
            tmp_score = score
            for j in range(Q):
                if A[abcd[j][1]-1] - A[abcd[j][0]-1] == abcd[j][2]:
                    tmp_score += abcd[j][3]
            max_score = max(max_score, dfs(A, M, Q, abcd, index+1, tmp_score))
        return max_score
