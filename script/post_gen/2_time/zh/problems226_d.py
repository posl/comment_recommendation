Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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

    #print(t)
    #print(k)
    #print(a)

    # 从第n-1个开始逆向遍历
    # 如果有前置步骤，就加上前置步骤的时间
    # 如果没有前置步骤，就直接加上自己的时间
    # 选出最大的时间
    # 重复这个过程
    # 直到第一个动作为止
    #print("t[0] = ", t[0])
    #print("k[0] = ", k[0])
    #print("a[0] = ", a[0])
    #print("len(a[0]) = ", len(a[0]))
    #print("a[0][0] = ", a[0][0])
    #print("a[0][1] = ", a[0][1])
    #print("a[0][2] = ", a[0][2])
    #print("a[0][3] = ", a[0][3])
    #print("a[0][4] = ", a[0][4])
    #print("a[0][5] = ", a[0][5])
    #print("a[0][6] = ", a[0][6])
    #print("a[0][7] = ", a[0][7])
    #print("a[0][8] = ", a[0][8])
    #print("a[0][9] = ", a[0][9])
    #print("a[0][10] = ", a[0][10])

    #print("t[1] = ", t[1])
    #print("k[1] = ", k[1])
    #print("a[1] = ", a[1])
    #print("len(a[1]) = ", len(a[1]))
    #print("a[1][0] = ", a[

=======
Suggestion 2

def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K[i]):
            dp[A[i][j]] = max(dp[A[i][j]], dp[i] + T[i])
    ans = max(dp) + T[N]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    t = [0] * (n + 1)
    k = [0] * (n + 1)
    a = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        t[i], k[i] = map(int, input().split())
        for j in range(k[i]):
            a[i][j] = int(input())

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = t[i]
        for j in range(k[i]):
            dp[i] = max(dp[i], dp[a[i][j]] + t[i])
    print(max(dp))

=======
Suggestion 4

def main():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        line = input().split()
        T.append(int(line[0]))
        K.append(int(line[1]))
        A.append([])
        for j in range(K[i]):
            A[i].append(int(line[2+j]))
    #print(T)
    #print(K)
    #print(A)
    D = [0] * N
    for i in range(N):
        if K[i] == 0:
            D[i] = T[i]
        else:
            D[i] = T[i] + max([D[j] for j in A[i]])
    print(max(D))

main()

=======
Suggestion 5

def solve():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        line = list(map(int, input().split()))
        T[i] = line[0]
        K[i] = line[1]
        A[i] = line[2:]
    dp = [0] * N
    for i in range(N):
        if not A[i]:
            dp[i] = T[i]
        else:
            dp[i] = min([dp[a] for a in A[i]]) + T[i]
    print(max(dp))

=======
Suggestion 6

def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(K[i]):
            dp[A[i][j]] = max(dp[A[i][j]], dp[i] + T[i])
    print(max(dp) + T[N])

=======
Suggestion 7

def main():
    # 读入数据
    # N = 3
    # T = [3, 5, 7]
    # K = [0, 1, 1]
    # A = [[], [1], [1]]
    # N = 5
    # T = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
    # K = [0, 0, 0, 0, 4]
    # A = [[], [], [], [], [1, 2, 3, 4]]
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        T_i, K_i, *A_i = map(int, input().split())
        T.append(T_i)
        K.append(K_i)
        A.append(A_i)

    # print(N, T, K, A)
    # 从后往前遍历
    # dp[i]: 学习第i步所需的最少时间
    # dp[i] = max(dp[A[i][j]] + T[A[i][j]] for j in range(K[i]))
    # print(A)
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        if K[i] == 0:
            dp[i] = T[i]
        else:
            dp[i] = max(dp[A[i][j]] + T[A[i][j]] for j in range(K[i]))

    print(max(dp))

=======
Suggestion 8

def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[0] * N for i in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        for j in range(1, K[i] + 1):
            A[i][j] = int(input())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, K[i] + 1):
            dp[i] = max(dp[i], dp[A[i][j]] + T[A[i][j]])
    print(dp[N] + T[N])

=======
Suggestion 9

def solve():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        t_k_a = input().split()
        T.append(int(t_k_a[0]))
        K.append(int(t_k_a[1]))
        A.append([int(a) for a in t_k_a[2:]])
    # print(N, T, K, A)
    # print(T)
    # print(K)
    # print(A)
    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])
    # print(A[9])
    # print(A[10])
    # print(A[11])
    # print(A[12])
    # print(A[13])
    # print(A[14])
    # print(A[15])
    # print(A[16])
    # print(A[17])
    # print(A[18])
    # print(A[19])
    # print(A[20])
    # print(A[21])
    # print(A[22])
    # print(A[23])
    # print(A[24])
    # print(A[25])
    # print(A[26])
    # print(A[27])
    # print(A[28])
    # print(A[29])
    # print(A[30])
    # print(A[31])
    # print(A[32])
    # print(A[33])
    # print(A[34])
    # print(A[35])
    # print(A[36])
    # print(A[37])
    # print(A[38])
    # print(A[39])
    # print(A[40])
    # print(A[41])
    # print(A[42])
    # print(A[43])
    # print(A[44])
    # print(A[45])
    # print(A[46])
    # print(A[47])
    # print(A[48])
    # print(A[49])
    # print(A[50])
    # print(A[51])
    # print(A[52])
    # print(A[53])
    # print(A[54])
    # print(A[55])
    # print(A[56])
    #
