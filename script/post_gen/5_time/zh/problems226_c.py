Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input().strip())
    t = []
    k = []
    a = []
    for i in range(n):
        line = input().strip().split()
        t.append(int(line[0]))
        k.append(int(line[1]))
        a.append(list(map(int, line[2:])))
    return n, t, k, a

=======
Suggestion 2

def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for i in range(n)]
    for i in range(n):
        t[i], k[i], *a[i] = map(int, input().split())
    dp = [0] * n
    for i in range(n):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            dp[i] = max(dp[j] for j in a[i]) + t[i]
    print(max(dp))

=======
Suggestion 3

def main():
    n = int(input())
    t = [0]*(n+1)
    k = [0]*(n+1)
    a = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        t[i],k[i] = map(int,input().split())
        a[i] = list(map(int,input().split()))
    dp = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(k[i]):
            dp[i] = max(dp[i],dp[a[i][j]]+t[a[i][j]])
        dp[i] = max(dp[i],dp[i-1]+t[i])
    print(dp[n])

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def main():
    n = int(input())
    t = [0] * (n + 1)
    k = [0] * (n + 1)
    a = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i] + t[i])
    print(max(dp) + t[n])

main()

=======
Suggestion 6

def main():
    n = int(input())
    t = [0] * (n+1)
    k = [0] * (n+1)
    a = [0] * (n+1)
    for i in range(1,n+1):
        t[i],k[i] = map(int,input().split())
        a[i] = list(map(int,input().split()))
    dp = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = t[i]
        for j in range(k[i]):
            dp[i] = max(dp[i],dp[a[i][j]]+t[i])
    print(dp[n])

=======
Suggestion 7

def solve():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
        A[i] = [a - 1 for a in A[i]]

    dp = [0] * N
    for i in range(N):
        if not A[i]:
            dp[i] = T[i]
        else:
            for j in A[i]:
                dp[i] = max(dp[i], dp[j] + T[i])

    print(max(dp))

=======
Suggestion 8

def main():
    #input
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t_temp, k_temp, *a_temp = map(int, input().split())
        t.append(t_temp)
        k.append(k_temp)
        a.append(a_temp)

    #init
    dp = [0 for i in range(n+1)]

    #dp
    for i in range(n):
        dp[a[i][0]] = max(dp[a[i][0]], dp[i+1] + t[i])
        for j in range(1, k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i+1])

    #output
    print(dp[n])

=======
Suggestion 9

def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t1,k1,*a1 = map(int,input().split())
        t.append(t1)
        k.append(k1)
        a.append(a1)
    print(t)
    print(k)
    print(a)
    print("end")

=======
Suggestion 10

def main():
    pass
