Synthesizing 10/10 solutions

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
    ans = 0
    for i in range(1, M + 1):
        A = [i]
        ans = max(ans, dfs(N, M, Q, a, b, c, d, A))
    print(ans)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    a, b, c, d = [], [], [], []
    for _ in range(Q):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
        c.append(tmp[2])
        d.append(tmp[3])
    ans = 0
    for i in range(1, M+1):
        A = [i]
        ans = max(ans, dfs(N, M, Q, A, a, b, c, d))
    print(ans)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N + 1)
    for i in range(Q):
        a, b, c, d = map(int, input().split())
        A[a - 1] += 1
        A[b] -= 1
    for i in range(N):
        A[i + 1] += A[i]
    print(sum(sorted(A[:N])[:M]))

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]

    ans = 0

    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            ans = max(ans, score)
            return

        A.append(A[-1])
        while A[-1] <= M:
            dfs(A)
            A[-1] += 1
        A.pop()

    dfs([1])

    print(ans)

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(Q)]
    print(solve(N, M, Q, L))

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    ABCD = [list(map(int, input().split())) for i in range(Q)]
    ans = 0
    for A in itertools.combinations_with_replacement(range(1, M + 1), N):
        score = 0
        for a, b, c, d in ABCD:
            if A[b - 1] - A[a - 1] == c:
                score += d
        ans = max(ans, score)
    print(ans)

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N+1)
    A[0] = 1
    A[N] = M
    q = []
    for i in range(Q):
        q.append(list(map(int, input().split())))
    print(calc(N, M, q, A))

=======
Suggestion 8

def main():
    # Read input
    N, M, Q = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    # Initialize
    A = [1] * N
    score = 0
    max_score = 0

    # Loop
    while True:
        # Update score
        for a, b, c, d in queries:
            if A[b-1] - A[a-1] == c:
                score += d
        max_score = max(max_score, score)
        score = 0

        # Increment
        A[0] += 1
        for i in range(N):
            if A[i] > M:
                if i == N-1:
                    return max_score
                A[i] = 1
                A[i+1] += 1

=======
Suggestion 9

def main():

    # Read input
    N, M, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(Q)]

    # Initialize
    ans = 0
    A = sorted(A, key=lambda x: x[3], reverse=True)
    for a in A:
        if a[0] == 1:
            a.append([1, M])
        elif a[1] == N:
            a.append([1, M])
        else:
            a.append([a[0]-1, a[1]+1])

    # Recursive function
    def rec(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, ans):
        if len(A) == 0:
            ans = max(ans, sum(B))
            return ans
        else:
            a = A.pop()
            for i in range(a[2]):
                for j in range(a[2]-i):
                    if i+j == a[2]:
                        if a[0] <= a[3][0] <= a[1]:
                            B[a[3][0]-1] += 1
                        if a[0] <= a[3][1] <= a[1]:
                            B[a[3][1]-1] += 1
                        ans = rec(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, ans)
                        if a[0] <= a[3][0] <= a[1]:
                            B[a[3][0]-1] -= 1
                        if a[0] <= a[3][1] <= a[1]:

=======
Suggestion 10

def solve(N,M,Q,ABCD):
    # write your code
    return 0
