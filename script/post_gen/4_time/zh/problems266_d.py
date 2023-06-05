Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t = []
    x = []
    a = []
    for i in range(n):
        t_x_a = list(map(int, input().split()))
        t.append(t_x_a[0])
        x.append(t_x_a[1])
        a.append(t_x_a[2])
    #print(t)
    #print(x)
    #print(a)
    #print(t[0])
    #print(x[0])
    #print(a[0])
    sum = 0
    for i in range(n):
        if i == 0:
            if t[i] >= x[i]:
                sum += a[i]
        else:
            if t[i] - t[i-1] >= abs(x[i] - x[i-1]):
                sum += a[i]
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    txa = []
    for i in range(n):
        txa.append(list(map(int, input().split())))
    # print(txa)
    # print(txa[0][0])
    # print(txa[0][1])
    # print(txa[0][2])
    # print(txa[1][0])
    # print(txa[1][1])
    # print(txa[1][2])
    # print(txa[2][0])
    # print(txa[2][1])
    # print(txa[2][2])
    # print(txa[3][0])
    # print(txa[3][1])
    # print(txa[3][2])
    # print(txa[4][0])
    # print(txa[4][1])
    # print(txa[4][2])
    # print(txa[5][0])
    # print(txa[5][1])
    # print(txa[5][2])
    # print(txa[6][0])
    # print(txa[6][1])
    # print(txa[6][2])
    # print(txa[7][0])
    # print(txa[7][1])
    # print(txa[7][2])
    # print(txa[8][0])
    # print(txa[8][1])
    # print(txa[8][2])
    # print(txa[9][0])
    # print(txa[9][1])
    # print(txa[9][2])
    # print(txa[10][0])
    # print(txa[10][1])
    # print(txa[10][2])
    # print(txa[11][0])
    # print(txa[11][1])
    # print(txa[11][2])
    # print(txa[12][0])
    # print(txa[12][1])
    # print(txa[12][2])
    # print(txa[13][0])
    # print(txa[13][1])
    # print(txa[13][2])
    # print(txa[14][0])
    # print(txa[14][1])
    # print(txa[14][2])
    # print(txa[15][0])
    #

=======
Suggestion 3

def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort()
    ans = 0
    for i in range(n):
        t, x, a = snuke[i]
        if x == 0:
            ans += a
        elif x == 1:
            if snuke[i - 1][1] == 0:
                ans += a
            else:
                ans += max(a - snuke[i - 1][2], 0)
        elif x == 2:
            if i + 1 < n and snuke[i + 1][1] == 3:
                ans += max(a - snuke[i + 1][2], 0)
            else:
                ans += a
        elif x == 3:
            if i + 1 < n and snuke[i + 1][1] == 2:
                ans += max(a - snuke[i + 1][2], 0)
            else:
                ans += a
        else:
            if i + 1 < n and snuke[i + 1][1] == 1:
                ans += max(a - snuke[i + 1][2], 0)
            else:
                ans += a
    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    x = [0] * (n+1)
    t = [0] * (n+1)
    a = [0] * (n+1)
    for i in range(1, n+1):
        t[i], x[i], a[i] = map(int, input().split())
    dp = [[0]*5 for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(5):
            dp[i][j] = dp[i-1][j]
        if x[i] == 0:
            dp[i][0] = max(dp[i][0], dp[i-1][0] + a[i])
        elif x[i] == 1:
            dp[i][1] = max(dp[i][1], dp[i-1][0] + a[i])
            dp[i][0] = max(dp[i][0], dp[i-1][1] + a[i])
        elif x[i] == 2:
            dp[i][2] = max(dp[i][2], dp[i-1][1] + a[i])
            dp[i][1] = max(dp[i][1], dp[i-1][2] + a[i])
        elif x[i] == 3:
            dp[i][3] = max(dp[i][3], dp[i-1][2] + a[i])
            dp[i][2] = max(dp[i][2], dp[i-1][3] + a[i])
        elif x[i] == 4:
            dp[i][4] = max(dp[i][4], dp[i-1][3] + a[i])
            dp[i][3] = max(dp[i][3], dp[i-1][4] + a[i])
    print(max(dp[n][0], dp[n][1], dp[n][2], dp[n][3], dp[n][4]))

solve()

=======
Suggestion 5

def main():
    N = int(input())
    T = [0] * (N + 1)
    X = [0] * (N + 1)
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i], X[i], A[i] = map(int, input().split())
    T[0] = 0
    X[0] = 0
    A[0] = 0
    maxA = [0] * (N + 1)
    for i in range(1, N + 1):
        maxA[i] = max(maxA[i - 1], A[i])
    ans = 0
    for i in range(1, N + 1):
        if (T[i] - T[i - 1]) >= abs(X[i] - X[i - 1]):
            if ((T[i] - T[i - 1]) - abs(X[i] - X[i - 1])) % 2 == 0:
                ans = max(ans, maxA[i])
            else:
                ans = max(ans, maxA[i - 1], maxA[i])
        else:
            ans = max(ans, maxA[i - 1], maxA[i])
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append([t, x, a])
    snuke.sort()
    #print(snuke)
    max_size = 0
    for i in range(n):
        if snuke[i][0] - snuke[i][1] >= 0:
            max_size += snuke[i][2]
    print(max_size)

=======
Suggestion 7

def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))

    snuke.sort(key=lambda x: x[0])
    t = 0
    x = 0
    max_a = 0
    for i in range(n):
        if snuke[i][0] >= abs(snuke[i][1] - x) + t:
            max_a += snuke[i][2]
            t = snuke[i][0]
            x = snuke[i][1]
    print(max_a)

=======
Suggestion 8

def main():
    # 读入数据
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    # 从后往前，计算每个时刻能抓到的最大值
    # dp[i]表示从第i个时刻到第N个时刻，能抓到的最大值
    # dp[i] = max(dp[i+1], dp[i+1] - (T[i+1] - T[i]) + A[i+1])
    dp = [0] * (N+1)
    for i in range(N-1, -1, -1):
        dp[i] = max(dp[i+1], dp[i+1] - (T[i+1] - T[i]) + A[i+1])
    # 从前往后，计算每个时刻能抓到的最大值
    # dp[i]表示从第0个时刻到第i个时刻，能抓到的最大值
    # dp[i] = max(dp[i-1], dp[i-1] - (T[i] - T[i-1]) + A[i])
    for i in range(1, N+1):
        dp[i] = max(dp[i-1], dp[i-1] - (T[i] - T[i-1]) + A[i])
    # 打印结果
    print(dp[N])
    return

=======
Suggestion 9

def problems266_d():
    n = int(input())
    txa = []
    for i in range(n):
        txa.append(list(map(int, input().split())))
    txa.insert(0, [0, 0, 0])
    ans = 0
    for i in range(1, n+1):
        time = txa[i][0] - txa[i-1][0]
        dis = abs(txa[i][1] - txa[i-1][1])
        if dis > time:
            print('No')
            return
        else:
            if (time - dis) % 2 == 1:
                print('No')
                return
            else:
                ans += txa[i][2]
    print('Yes')
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    txa = [list(map(int, input().split())) for i in range(n)]
    txa.insert(0, [0, 0, 0])
    result = 0
    for i in range(1, len(txa)):
        result += max(0, txa[i][2] - (txa[i][0] - txa[i - 1][0] - abs(txa[i][1] - txa[i - 1][1])))
    print(result)
