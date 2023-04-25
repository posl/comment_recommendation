Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    a, b, c, d = [], [], [], []
    for i in range(Q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
        d.append(d_i)
    print(solve(N, M, Q, a, b, c, d))

=======
Suggestion 2

def   main (): 
     n ,   m ,   q   =   map ( int ,   input (). split ()) 
     a ,   b ,   c ,   d   =   [],   [],   [],   [] 
     for   _   in   range ( q ): 
         _a ,   _b ,   _c ,   _d   =   map ( int ,   input (). split ()) 
         a . append ( _a ) 
         b . append ( _b ) 
         c . append ( _c ) 
         d . append ( _d ) 

     ans   =   0 
     for   i   in   range ( 1 ,   m   +   1 ): 
         ans   =   max ( ans ,   dfs ([ i ],   n ,   m ,   q ,   a ,   b ,   c ,   d )) 
     print ( ans )

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        x, y, z, w = map(int, input().split())
        a.append(x)
        b.append(y)
        c.append(z)
        d.append(w)

    A = [1] * N
    ans = 0
    while True:
        score = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                score += d[i]
        ans = max(ans, score)

        i = N - 1
        while i >= 0 and A[i] == M:
            i -= 1
        if i < 0:
            break
        A[i] += 1
        for j in range(i + 1, N):
            A[j] = A[i]

    print(ans)

=======
Suggestion 4

def main():
    n, m, q = map(int, input().split())
    a = []
    b = []
    c = []
    d = []
    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
        d.append(di)
    ans = 0
    def dfs(s, A):
        global ans
        if len(A) == n:
            score = 0
            for i in range(q):
                if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                    score += d[i]
            ans = max(ans, score)
            return
        for i in range(s, m + 1):
            A.append(i)
            dfs(i, A)
            A.pop()
    dfs(1, [])
    print(ans)

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    Qs = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        Qs.append((a, b, c, d))
    ans = 0
    for A in itertools.product(range(1, M + 1), repeat=N):
        score = 0
        for a, b, c, d in Qs:
            if A[b - 1] - A[a - 1] == c:
                score += d
        ans = max(ans, score)
    print(ans)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    L = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        L.append((a-1, b, c, d))
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in L:
                if A[b] - A[a] == c:
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
Suggestion 7

def solve():
    N, M, Q = map(int, input().split())
    A = [0] * Q
    for i in range(Q):
        A[i] = list(map(int, input().split()))
    ans = 0
    def dfs(cur, last):
        nonlocal ans
        if cur == N:
            score = 0
            for a, b, c, d in A:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            ans = max(ans, score)
            return
        for i in range(last, M + 1):
            A[cur] = i
            dfs(cur + 1, i)
    dfs(0, 1)
    print(ans)

=======
Suggestion 8

def solve(N, M, Q, queries):
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == N:
            score = 0
            for a, b, c, d in queries:
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
            return
        for i in range(1, M+1):
            if len(A) == 0 or A[-1] <= i:
                A.append(i)
                dfs(A)
                A.pop()
    dfs([])
    return ans

=======
Suggestion 9

def main():
    #write your code here
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[N-1] = M
    ans = 0
    for i in range(Q):
        a,b,c,d = map(int, input().split())
        if A[a-1] <= c and c <= A[b-1]:
            ans += d
    print(ans)

=======
Suggestion 10

def main():
    N, M, Q = map(int, input().split())
    # A = [0] * N
    A = [1] * N
    score = 0
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        if A[b-1] - A[a-1] == c:
            score += d
    print(score)
