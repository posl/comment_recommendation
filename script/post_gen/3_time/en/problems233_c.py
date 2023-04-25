Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l[0])
        A.append(l[1:])
    #print(N, X, L, A)
    #print(N, X, L, A, file=sys.stderr)
    ans = 0
    for i in range(1 << N):
        cnt = 0
        prod = 1
        for j in range(N):
            if ((i >> j) & 1):
                cnt += 1
                prod *= A[j][0]
            else:
                prod *= A[j][1]
        if (prod == X):
            ans += cnt
    print(ans)

=======
Suggestion 2

def solve():
    N,X = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        l = list(map(int,input().split()))
        L.append(l[0])
        A.append(l[1:])
    
    #dp[i][j] = i番目までのバッグの中から選んだj個の積がXの倍数であるような選び方の個数
    dp = [[0 for i in range(10**5+1)] for j in range(N)]
    for i in range(N):
        for j in range(L[i]):
            if A[i][j] == X:
                dp[i][1] += 1
            elif X%A[i][j] == 0:
                dp[i][0] += 1
    for i in range(1,N):
        for j in range(10**5+1):
            for k in range(L[i]):
                if j == 0:
                    if X%A[i][k] == 0:
                        dp[i][j] += dp[i-1][j]
                else:
                    if A[i][k] == X:
                        dp[i][j] += dp[i-1][j-1]
                    elif X%A[i][k] == 0:
                        dp[i][j] += dp[i-1][j-1]
    print(dp[N-1][0]+dp[N-1][1]+dp[N-1][2])
solve()

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, 2**N):
        bit = bin(i)[2:].zfill(N)
        cnt = 1
        for j in range(N):
            if bit[j] == '1':
                cnt *= L[j][1+bit.count('1')]
        if cnt == X:
            ans += 1
    print(ans)

=======
Suggestion 4

def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        a, b = b % a, a
    return b

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2**N):
        b = bin(i)[2:].zfill(N)
        p = 1
        for j in range(N):
            if b[j] == '1':
                p *= L[j][1]
            else:
                p *= L[j][2]
        if p == X:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    print(solve(N, X, L))

=======
Suggestion 7

def main():
    input = sys.stdin.readline
    N, X = map(int, input().split())
    L = [None] * N
    A = [None] * N
    for i in range(N):
        L[i], *A[i] = map(int, input().split())
    #dp[i][j]: the number of ways to pick i balls so that the product of the numbers written on the picked balls is j
    dp = [[0] * (X + 1) for _ in range(N + 1)]
    dp[0][1] = 1
    for i in range(N):
        for j in range(X + 1):
            for k in range(L[i]):
                if j * A[i][k] <= X:
                    dp[i + 1][j * A[i][k]] += dp[i][j]
    print(dp[N][X])

=======
Suggestion 8

def get_primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    #sieve of eratosthenes
    limit = n + 1
    not_prime = [False] * limit
    primes = []
    for i in range(2, limit):
        if not_prime[i]:
            continue
        for f in range(i * 2, limit, i):
            not_prime[f] = True
        primes.append(i)
    return primes

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    l = [list(map(int, input().split())) for i in range(n)]
    l = [[0, 0]] + l
    dp = [[0] * (x + 1) for i in range(n + 1)]
    dp[0][1] = 1
    for i in range(1, n + 1):
        for j in range(x + 1):
            for k in range(l[i][0]):
                if j * l[i][k + 1] <= x:
                    dp[i][j * l[i][k + 1]] += dp[i - 1][j]
    print(dp[n][x])

=======
Suggestion 10

def solve():
    from math import gcd
    from collections import Counter
    N,X=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(N)]
    L=[a[0] for a in A]
    C=[a[1:] for a in A]
    D=[Counter() for _ in range(N)]
    for i in range(N):
        for j in range(L[i]):
            D[i][C[i][j]]+=1
    E=[Counter() for _ in range(N)]
    E[0]=D[0]
    for i in range(1,N):
        for k,v in E[i-1].items():
            for j in range(L[i]):
                g=gcd(k,C[i][j])
                E[i][g]+=v*D[i][C[i][j]]
    ans=0
    for k,v in E[N-1].items():
        if X%k==0 and X//k in E[N-1]:
            ans+=v*E[N-1][X//k]
    print(ans)

solve()

I solved this problem using the Chinese Remainder Theorem. The solution is here.

I solved this problem using a DP. Th
