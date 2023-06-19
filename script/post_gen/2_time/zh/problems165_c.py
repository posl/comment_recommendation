Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, q = map(int, input().split())
    abcd = []
    for i in range(q):
        abcd.append(list(map(int, input().split())))
    a = [1] * n
    def dfs(i):
        if i == n:
            return
        for j in range(a[i - 1], m + 1):
            a[i] = j
            dfs(i + 1)
            print(a)
    dfs(1)
    print(a)
main()

=======
Suggestion 2

def main():
    N, M, Q = [int(i) for i in input().split()]
    l = []
    for i in range(Q):
        l.append([int(i) for i in input().split()])
    print(l)
    print(N, M, Q)

=======
Suggestion 3

def main():
    n,m,q = map(int,input().split())
    a = [0 for i in range(q)]
    b = [0 for i in range(q)]
    c = [0 for i in range(q)]
    d = [0 for i in range(q)]
    for i in range(q):
        a[i],b[i],c[i],d[i] = map(int,input().split())
    print(a)
    print(b)
    print(c)
    print(d)

=======
Suggestion 4

def max_score(N, M, Q, a, b, c, d):
    score = 0
    return score

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for _ in range(Q)]
    A = [1] * N
    max_score = 0
    while True:
        score = 0
        for a, b, c, d in ABCD:
            if A[b - 1] - A[a - 1] == c:
                score += d
        max_score = max(max_score, score)
        for i in range(N - 1, -1, -1):
            if A[i] < M:
                A[i] += 1
                break
            else:
                A[i] = 1
        else:
            break
    print(max_score)

=======
Suggestion 6

def get_max_score(A, N, M, Q, a, b, c, d):
    max_score = 0
    for i in range(1, 2**N):
        A = [int(x) for x in bin(i)[2:]]
        A = [0] * (N - len(A)) + A
        if sum(A) == 0:
            continue
        score = 0
        for j in range(Q):
            if A[b[j] - 1] - A[a[j] - 1] == c[j]:
                score += d[j]
        max_score = max(max_score, score)
    return max_score

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0

    def dfs(A, B):
        nonlocal ans
        if len(B) == N:
            score = 0
            for a, b, c, d in A:
                if B[b - 1] - B[a - 1] == c:
                    score += d
            ans = max(ans, score)
        else:
            for i in range(B[-1] if B else 1, M + 1):
                dfs(A, B + [i])

    dfs(A, [])
    print(ans)

=======
Suggestion 8

def get_score(n, m, q, a, b, c, d):
    score = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, q+1):
                if a[k] == i and b[k] == j:
                    score += d[k]
    return score

=======
Suggestion 9

def main():
    n, m, q = map(int, input().split())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == n:
            s = 0
            for i in range(q):
                if A[query[i][1]-1] - A[query[i][0]-1] == query[i][2]:
                    s += query[i][3]
            ans = max(ans, s)
            return
        for i in range(A[-1], m+1):
            dfs(A+[i])
    for i in range(1, m+1):
        dfs([i])
    print(ans)

=======
Suggestion 10

def max_score(n, m, q, abcd_list):
    # n = 3
    # m = 4
    # q = 3
    # abcd_list = [[1, 3, 3, 100], [1, 2, 2, 10], [2, 3, 2, 10]]
    # n = 4
    # m = 6
    # q = 10
    # abcd_list = [[2, 4, 1, 86568], [1, 4, 0, 90629], [2, 3, 0, 90310], [3, 4, 1, 29211], [3, 4, 3, 78537], [3, 4, 2, 8580], [1, 2, 1, 96263], [1, 4, 2, 2156], [1, 2, 0, 94325], [1, 4, 3, 94328]]
    # n = 10
    # m = 10
    # q = 1
    # abcd_list = [[1, 10, 9, 1]]
    # n = 2
    # m = 10
    # q = 1
    # abcd_list = [[1, 2, 0, 1]]
    # n = 2
    # m = 10
    # q = 1
    # abcd_list = [[1, 2, 1, 1]]
    # n = 2
    # m = 10
    # q = 1
    # abcd_list = [[1, 2, 2, 1]]
    # n = 2
    # m = 10
    # q = 1
    # abcd_list = [[1, 2, 3, 1]]
    # n = 2
    # m = 10
    # q = 1
    # abcd_list = [[1, 2, 4, 1]]
    # n = 2
    # m = 10
    # q = 1
    # abcd_list = [[1, 2,
