Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        T[i], K[i], *A[i] = map(int, input().split())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in A[i]:
            dp[i] = max(dp[i], dp[j] + T[j])
        dp[i] += T[i]
    print(dp[N])

=======
Suggestion 2

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    #print(N)
    #print(T)
    #print(K)
    #print(A)
    #print("end of input")
    #print("")

    #dp[i] = minimum time to learn move i
    dp = [0] * (N+1)
    dp[0] = 0
    for i in range(N):
        dp[i+1] = dp[i] + T[i]
        for j in range(K[i]):
            dp[i+1] = min(dp[i+1], dp[A[i][j]-1] + T[i])
    #print(dp)
    print(dp[N])

=======
Suggestion 3

def main():
    n = int(input())
    t = []
    a = []
    for i in range(n):
        t_i, k_i, *a_i = map(int, input().split())
        t.append(t_i)
        a.append(a_i)
    #print(n, t, a)
    #print(t[-1])
    #print(a[-1])
    #print(a[-1][-1])
    #print(a[-1][-1]-1)
    #print(a[-1][a[-1][-1]-1])
    #print(t[-1] - t[a[-1][-1]-1])
    #print(a[-1][-1]-1)
    #print(a[-1][a[-1][-1]-1])
    #print(a[-1][a[-1][-1]-1]-1)
    #print(t[-1] - t[a[-1][a[-1][-1]-1]-1])
    #print(a[-1][-1]-1)
    #print(a[-1][a[-1][-1]-1])
    #print(a[-1][a[-1][-1]-1]-1)
    #print(a[-1][a[-1][a[-1][-1]-1]-1])
    #print(t[-1] - t[a[-1][a[-1][a[-1][-1]-1]-1]-1])
    #print(a[-1][-1]-1)
    #print(a[-1][a[-1][-1]-1])
    #print(a[-1][a[-1][-1]-1]-1)
    #print(a[-1][a[-1][a[-1][-1]-1]-1])
    #print(a[-1][a[-1][a[-1][-1]-1]-1]-1)
    #print(t[-1] - t[a[-1][a[-1][a[-1][-1]-1]-1]-1])
    #print(a[-1][-1]-1)
    #print(a[-1][a[-1][-1]-1])
    #print(a[-1][a[-1][-1]-1]-1)
    #print(a[-1][a[-1][a[-1][-1]-1]-1])
    #print(a[-1][a[-1][a[-1][-1]-1]-1]-1)
    #print(a[-1][a[-1

=======
Suggestion 4

def main():
    n = int(input())
    t = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i], k, *a = map(int, input().split())
        for j in range(k):
            t[i] = max(t[i], t[a[j]] + 1)
    print(t[n])

=======
Suggestion 5

def solve():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [[] for _ in range(n)]
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        if k[i] > 0:
            a[i] = list(map(int, input().split()))
            for j in range(k[i]):
                a[i][j] -= 1
    # print(t)
    # print(k)
    # print(a)
    dp = [0] * n
    for i in range(n):
        if k[i] == 0:
            dp[i] = t[i]
        else:
            dp[i] = max([dp[j] for j in a[i]]) + t[i]
    # print(dp)
    print(dp[n - 1])
    return 0

=======
Suggestion 6

def readinput():
    n=int(input())
    t=[]
    k=[]
    a=[]
    for _ in range(n):
        line=input()
        t1,k1,a1=map(int,line.split())
        t.append(t1)
        k.append(k1)
        a.append(a1)
    return n,t,k,a

=======
Suggestion 7

def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        Ti, Ki, *Ai = map(int, input().split())
        T.append(Ti)
        A.append(Ai)

    #print(N)
    #print(T)
    #print(A)

    #print(T[0])
    #print(A[0])

    #print(T[1])
    #print(A[1])

    #print(T[2])
    #print(A[2])

    #print(T[3])
    #print(A[3])

    #print(T[4])
    #print(A[4])

    #print(T[5])
    #print(A[5])

    #print(T[6])
    #print(A[6])

    #print(T[7])
    #print(A[7])

    #print(T[8])
    #print(A[8])

    #print(T[9])
    #print(A[9])

    #print(T[10])
    #print(A[10])

    #print(T[11])
    #print(A[11])

    #print(T[12])
    #print(A[12])

    #print(T[13])
    #print(A[13])

    #print(T[14])
    #print(A[14])

    #print(T[15])
    #print(A[15])

    #print(T[16])
    #print(A[16])

    #print(T[17])
    #print(A[17])

    #print(T[18])
    #print(A[18])

    #print(T[19])
    #print(A[19])

    #print(T[20])
    #print(A[20])

    #print(T[21])
    #print(A[21])

    #print(T[22])
    #print(A[22])

    #print(T[23])
    #print(A[23])

    #print(T[24])
    #print(A[24])

    #print(T[25])
    #print(A[25])

    #print(T[26])
    #print(A[26])

    #print(T[27])
    #print(A[27])

    #print(T[28])
    #print(A[28])

    #print(T[29])
    #print(A[29])

    #print(T[30])
    #print(A[30])

=======
Suggestion 8

def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        temp = list(map(int, input().split()))
        T.append(temp[0])
        A.append(temp[2:])
    time = [0 for i in range(N)]
    for i in range(N):
        if A[i] == []:
            time[i] = T[i]
        else:
            for j in A[i]:
                time[i] = max(time[i], time[j-1] + T[i])
    print(max(time))

=======
Suggestion 9

def main():
    N = int(input())
    moves = [tuple(map(int, input().split())) for _ in range(N)]
    moves.sort(key=lambda x: x[0])
    moves.append((0, 0))
    times = [0] * (N + 1)
    for i in range(N):
        t, k, *a = moves[i]
        times[i + 1] = t + max(times[j] for j in a)
    print(times[-1])

=======
Suggestion 10

def main():
    N = int(input())
    moves = [list(map(int, input().split())) for _ in range(N)]
    moves = sorted(moves, key=lambda x: x[0])
    moves.reverse()

    # print(moves)
    # print(moves[0][0])

    sum = 0
    for i in range(N):
        if i == 0:
            sum += moves[i][0]
        else:
            if moves[i][0] == moves[i-1][0]:
                sum += moves[i][0]
            else:
                sum += moves[i][0] - moves[i][1]

    print(sum)
