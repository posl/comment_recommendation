Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, t, k, a):
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = dp[i] + t[i]
        for j in range(k[i]):
            dp[i + 1] = max(dp[i + 1], dp[a[i][j] - 1] + t[i])
    return dp[n]

=======
Suggestion 2

def solve():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    for i in range(1, N + 1):
        A[i].sort(reverse = True)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = T[i]
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j]] + T[i])
    print(dp[N])

solve()

=======
Suggestion 3

def calc_time(n, t, k, a):
    time = [0 for i in range(n)]
    for i in range(n):
        if k[i] == 0:
            time[i] = t[i]
        else:
            max_time = 0
            for j in range(k[i]):
                if time[a[i][j] - 1] > max_time:
                    max_time = time[a[i][j] - 1]
            time[i] = max_time + t[i]
    return max(time)

=======
Suggestion 4

def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        t.append(tmp[0])
        k.append(tmp[1])
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        if k[i] == 0:
            ans = max(ans, t[i])
        else:
            tmp = 0
            for j in range(k[i]):
                tmp = max(tmp, t[a[i][j]-1])
            ans = max(ans, tmp+t[i])
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[] for i in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = T[i]
        for j in range(K[i]):
            dp[i] = max(dp[i], dp[A[i][j]] + T[i])
    print(max(dp))

=======
Suggestion 6

def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t1, k1, *a1 = map(int, input().split())
        t.append(t1)
        k.append(k1)
        a.append(a1)
    #print(t)
    #print(k)
    #print(a)
    ans = 0
    for i in range(n):
        if k[i] == 0:
            ans += t[i]
        else:
            tmax = 0
            for j in range(k[i]):
                if tmax < t[a[i][j]-1]:
                    tmax = t[a[i][j]-1]
            t[i] += tmax
            ans += t[i]
    print(ans)

=======
Suggestion 7

def get_input():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        K.append(k)
        A.append(a)
    return N, T, K, A

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    t = []
    a = []
    for i in range(n):
        tmp = list(map(int,input().split()))
        t.append(tmp[0])
        a.append(tmp[2:])

    s = [0] * n
    for i in range(n):
        s[i] = t[i]
        if a[i]:
            for j in a[i]:
                s[i] = max(s[i],s[j-1] + t[i])
    print(max(s))

=======
Suggestion 10

def main():
    N = int(input())
    T = [0] * (N+1)
    K = [0] * (N+1)
    A = [0] * (N+1)
    for i in range(1,N+1):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    #print(T, K, A)
    #print(T[1], K[1], A[1])
    #print(T[2], K[2], A[2])
    #print(T[3], K[3], A[3])
    #print(T[4], K[4], A[4])
    #print(T[5], K[5], A[5])
    #print(T[6], K[6], A[6])
    #print(T[7], K[7], A[7])
    #print(T[8], K[8], A[8])
    #print(T[9], K[9], A[9])
    #print(T[10], K[10], A[10])
    #print(T[11], K[11], A[11])
    #print(T[12], K[12], A[12])
    #print(T[13], K[13], A[13])
    #print(T[14], K[14], A[14])
    #print(T[15], K[15], A[15])
    #print(T[16], K[16], A[16])
    #print(T[17], K[17], A[17])
    #print(T[18], K[18], A[18])
    #print(T[19], K[19], A[19])
    #print(T[20], K[20], A[20])
    #print(T[21], K[21], A[21])
    #print(T[22], K[22], A[22])
    #print(T[23], K[23], A[23])
    #print(T[24], K[24], A[24])
    #print(T[25], K[25], A[25])
    #print(T[26], K[26], A[26])
    #print(T[27], K[27], A[27])
    #print
