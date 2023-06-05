Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]

    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))

    dp = [0] * n
    for i in range(n):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            for j in a[i]:
                dp[i] = max(dp[i], dp[j - 1] + t[i])

    print(max(dp))

=======
Suggestion 2

def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        tmp = input().split()
        T.append(int(tmp[0]))
        K.append(int(tmp[1]))
        A.append(list(map(lambda x:int(x)-1, tmp[2:])))
    #print(T)
    #print(K)
    #print(A)
    #print('=====================')
    T = [0] + T
    K = [0] + K
    A = [[]] + A
    #print(T)
    #print(K)
    #print(A)
    #print('=====================')
    dp = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j]+1] + T[A[i][j]+1])
    #print(dp)
    print(dp[N] + T[N])

=======
Suggestion 3

def main():
    return 0

=======
Suggestion 4

def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t_i, k_i, *a_i = map(int, input().split())
        t.append(t_i)
        k.append(k_i)
        a.append(a_i)
    t_max = max(t)
    t_min = min(t)
    t_sum = sum(t)
    print(t_max + t_sum)

=======
Suggestion 5

def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        K.append(k)
        A.append(a)
    time = 0
    for i in range(N-1, -1, -1):
        if T[i] == 0:
            time = max(time, 0)
        else:
            time = max(time, T[i] + time)
    print(time)

main()

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    t = [0] * (n + 1)
    k = [0] * (n + 1)
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i] + t[i])
    print(max(dp) + t[n])

=======
Suggestion 8

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())
        A[i] = [a - 1 for a in A[i]]

    from collections import deque
    q = deque()
    for i in range(N):
        if K[i] == 0:
            q.append(i)

    dp = [0] * N
    while q:
        i = q.popleft()
        if A[i]:
            dp[i] = max(dp[j] for j in A[i]) + T[i]
        else:
            dp[i] = T[i]
        for j in range(N):
            if j in A[i]:
                A[j].remove(j)
                if not A[j]:
                    q.append(j)

    print(max(dp))

=======
Suggestion 9

def main():
    n = int(input())
    t = [0] * (n+1)
    k = [0] * (n+1)
    a = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        t[i], k[i], *a[i] = map(int, input().split())
    ans = 0
    for i in range(n, 0, -1):
        ans = max(ans, t[i] + max([t[j] for j in a[i]]))
    print(ans)
