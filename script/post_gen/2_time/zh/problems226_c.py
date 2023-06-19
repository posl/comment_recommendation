Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        a.append([])
        t1, k1, *a1 = map(int, input().split())
        t.append(t1)
        k.append(k1)
        for j in range(k1):
            a[i].append(a1[j])
    print(a)
    print(t)
    print(k)
    ans = 0
    for i in range(n):
        if k[i] == 0:
            ans = max(ans, t[i])
        else:
            ans = max(ans, t[i]+t[a[i][0]-1])
    print(ans)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def solve():
    pass

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
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i + 1], dp[i] + t[i])
        for j in range(k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i])
    print(dp[n])

=======
Suggestion 5

def main():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [0] * n
    for i in range(n):
        t[i], k[i], *a[i] = map(int, input().split())
    dp = [0] * n
    for i in range(n):
        for j in range(k[i]):
            dp[a[i][j]-1] = max(dp[a[i][j]-1], dp[i] + t[i])
    print(max(dp) + t[-1])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append([int(x) for x in input().split()])
    t = [0] * n
    for i in range(n):
        if s[i][1] == 0:
            t[i] = s[i][0]
        else:
            for j in range(s[i][1]):
                t[i] = max(t[i], t[s[i][2 + j] - 1] + s[i][0])
    print(max(t))

=======
Suggestion 7

def solve():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        t,k,*a = map(int,input().split())
        T.append(t)
        K.append(k)
        A.append(a)
    #print(T,K,A)
    #print(T[0],K[0],A[0])
    #print(T[1],K[1],A[1])
    #print(T[2],K[2],A[2])
    #print(T[3],K[3],A[3])
    #print(T[4],K[4],A[4])
    #print(T[5],K[5],A[5])
    #print(T[6],K[6],A[6])
    #print(T[7],K[7],A[7])
    #print(T[8],K[8],A[8])
    #print(T[9],K[9],A[9])
    #print(T[10],K[10],A[10])
    #print(T[11],K[11],A[11])
    #print(T[12],K[12],A[12])
    #print(T[13],K[13],A[13])
    #print(T[14],K[14],A[14])
    #print(T[15],K[15],A[15])
    #print(T[16],K[16],A[16])
    #print(T[17],K[17],A[17])
    #print(T[18],K[18],A[18])
    #print(T[19],K[19],A[19])
    #print(T[20],K[20],A[20])
    #print(T[21],K[21],A[21])
    #print(T[22],K[22],A[22])
    #print(T[23],K[23],A[23])
    #print(T[24],K[24],A[24])
    #print(T[25],K[25],A[25])
    #print(T[26],K[26],A[26])
    #print(T[27],K[27],A[27])
    #print(T[28],K[28],A[28])
    #print(T

=======
Suggestion 8

def solve(n, t, k, a):
    #print(n, t, k, a)
    dp = [0] * (n+1)
    for i in range(n):
        for j in range(k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i+1] + t[i])
    print(max(dp))

n = int(input())
t = []
k = []
a = []
for i in range(n):
    t_, k_ = map(int, input().split())
    t.append(t_)
    k.append(k_)
    a.append(list(map(int, input().split())))
solve(n, t, k, a)

=======
Suggestion 9

def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        T_i, K_i, *A_i = map(int, input().split())
        T.append(T_i)
        K.append(K_i)
        A.append(A_i)

    # print(N)
    # print(T)
    # print(K)
    # print(A)

    # print(T[1])
    # print(K[1])
    # print(A[1])

    # print(len(A[1]))
    # print(A[1][0])

    # print(A[1][0])
    # print(A[1][1])
    # print(A[1][2])
    # print(A[1][3])

    # print(A[1][0] < 1)
    # print(A[1][1] < 1)
    # print(A[1][2] < 1)
    # print(A[1][3] < 1)

    # print(A[1][0] < 2)
    # print(A[1][1] < 2)
    # print(A[1][2] < 2)
    # print(A[1][3] < 2)

    # print(A[1][0] < 3)
    # print(A[1][1] < 3)
    # print(A[1][2] < 3)
    # print(A[1][3] < 3)

    # print(A[1][0] < 4)
    # print(A[1][1] < 4)
    # print(A[1][2] < 4)
    # print(A[1][3] < 4)

    # print(A[1][0] < 5)
    # print(A[1][1] < 5)
    # print(A[1][2] < 5)
    # print(A[1][3] < 5)

    # print(A[1][0] < 6)
    # print(A[1][1] < 6)
    # print(A[1][2] < 6)
    # print(A[1][3] < 6)

    # print(A[1][0] < 7)
    # print(A[1][1] < 7)
    # print(A[
