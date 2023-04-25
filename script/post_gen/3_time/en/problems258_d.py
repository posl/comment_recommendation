Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A = sorted(A)
    B = sorted(B)
    A.append(10**9)
    B.append(10**9)

    ans = 0
    i = 0
    j = N - 1
    while X > 0:
        if A[i] < B[j]:
            ans += A[i]
            X -= 1
            i += 1
        else:
            ans += B[j]
            X -= 1
            j -= 1

    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort(reverse=True)

    #print(A)
    #print(B)

    ans = 0
    for i in range(N):
        if X > 0:
            if A[i] < B[i]:
                ans += A[i]
                X -= 1
            else:
                ans += B[i]
                X -= 1
        else:
            break

    if X > 0:
        ans += B[0] * X

    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i] + B[i]
    total -= min(B)
    print(total * (X - 1) + min(A) + min(B))

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    a = 0
    b = 0
    ans = 0
    while X > 0:
        if a == N:
            ans += B[b] * X
            b += 1
            X = 0
        elif b == N:
            ans += A[a] * X
            a += 1
            X = 0
        elif A[a] < B[b]:
            ans += A[a]
            a += 1
            X -= 1
        else:
            ans += B[b]
            b += 1
            X -= 1
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A[i] < B[i]:
            ans += A[i]
            X -= 1
        else:
            ans += B[i]
            X -= 1
    if X > 0:
        ans += X * B[N - 1]
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.append(0)
    B.append(0)
    ans = 0
    for i in range(N):
        if A[i] < B[i]:
            ans += A[i]
            X -= 1
            if X <= 0:
                break
            A[i] = 0
            B[i] = 0
        else:
            ans += B[i]
            B[i] = 0
    if X > 0:
        A.append(A[N])
        B.append(B[N])
        A[N] = 0
        B[N] = 0
        A[N+1] = 0
        B[N+1] = 0
        A[N] = min(A[N], A[N+1])
        B[N] = min(B[N], B[N+1])
        A[N+1] = 0
        B[N+1] = 0
        ans += min(A[N], B[N]) * X
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A = [0] + A
    B = [0] + B
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, X + 1):
            if j == 1:
                dp[i][j] = A[i] + B[i]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + A[i] + B[i], dp[i][j - 1] + B[i])
    print(dp[N][X])

=======
Suggestion 8

def main():
    N,X=map(int,input().split())
    A=[0]*(N+1)
    B=[0]*(N+1)
    for i in range(1,N+1):
        A[i],B[i]=map(int,input().split())
    dp=[[0]*(N+1) for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j]=min(dp[i-1][j]+A[i],dp[i-1][j-1]+A[i]+B[i])
    ans=10**18
    for i in range(N+1):
        ans=min(ans,dp[N][i]+(X-i)*B[N])
    print(ans)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    
    ans = 0
    for a, b in AB:
        ans += a
        X -= 1
        if X == 0:
            break
    if X > 0:
        ans += X * AB[-1][0] + X * AB[-1][1]
    print(ans)
