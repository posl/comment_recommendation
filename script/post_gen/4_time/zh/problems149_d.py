Synthesizing 10/10 solutions

=======
Suggestion 1

def max_score(n, k, r, s, p, t):
    score = 0
    for i in range(n):
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        else:
            score += s
    return score

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    # dp[i][j] : i回目までの戦いでjを出した場合の最大得点
    dp = [[0 for j in range(3)] for i in range(N)]

    # 初期化
    for i in range(N):
        if T[i] == 'r':
            dp[i][0] = P
        elif T[i] == 's':
            dp[i][1] = R
        else:
            dp[i][2] = S

    # dp
    for i in range(K, N):
        for j in range(3):
            dp[i][j] = max(dp[i - K][(j + 1) % 3], dp[i - K][(j + 2) % 3]) + dp[i][j]

    # print(dp)
    print(max(dp[N - 1]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            else:
                score += S
        else:
            if T[i] == "r":
                if T[i - K] == "r":
                    T = T[:i] + "x" + T[i + 1:]
                else:
                    score += P
            elif T[i] == "s":
                if T[i - K] == "s":
                    T = T[:i] + "x" + T[i + 1:]
                else:
                    score += R
            else:
                if T[i - K] == "p":
                    T = T[:i] + "x" + T[i + 1:]
                else:
                    score += S
    print(score)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    score = 0
    for i in range(N):
        if T[i] == 'r':
            if i >= K and T[i - K] == 'r':
                T = T[:i] + 'x' + T[i + 1:]
            else:
                score += P
        elif T[i] == 's':
            if i >= K and T[i - K] == 's':
                T = T[:i] + 'x' + T[i + 1:]
            else:
                score += R
        else:
            if i >= K and T[i - K] == 'p':
                T = T[:i] + 'x' + T[i + 1:]
            else:
                score += S
    print(score)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    # 读入数据
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # 初始化dp数组
    dp = [[0]*3 for i in range(N)]
    # 初始化dp数组的第一行
    if T[0] == 'r':
        dp[0][1] = P
        dp[0][2] = S
    elif T[0] == 's':
        dp[0][0] = R
        dp[0][2] = S
    else:
        dp[0][0] = R
        dp[0][1] = P
    # 递推
    for i in range(1, N):
        if T[i] == 'r':
            dp[i][0] = max(dp[i-1][1], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + P
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        elif T[i] == 's':
            dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + R
            dp[i][1] = max(dp[i-1][0], dp[i-1][2])
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        else:
            dp[i][0] = max(dp[i-1][1], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + S
            dp[i][2] = max(dp[i-1][0], dp[i-1][1])
        if i >= K:
            dp[i][0] = max(dp[i][0], dp[i-K][0])
            dp[i][1] = max(dp[i][1], dp[i-K][1])
            dp[i][2] = max(dp[i][2], dp[i-K][2])
    # 打印结果
    print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

=======
Suggestion 7

def get_max_score(n, k, r, s, p, t):
    score = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                score += p
            elif t[i] == 's':
                score += r
            else:
                score += s
        else:
            if t[i] == 'r':
                if t[i-k] == 'r':
                    t[i] = 'x'
                else:
                    score += p
            elif t[i] == 's':
                if t[i-k] == 's':
                    t[i] = 'x'
                else:
                    score += r
            else:
                if t[i-k] == 'p':
                    t[i] = 'x'
                else:
                    score += s
    return score

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    #print(N,K,R,S,P,T)
    #print(len(T))
    #print(T[0])
    #print(T[1])
    #print(T[2])
    #print(T[3])
    #print(T[4])
    #print(T[5])
    #print(T[6])
    #print(T[7])
    #print(T[8])
    #print(T[9])
    #print(T[10])
    #print(T[11])
    #print(T[12])
    #print(T[13])
    #print(T[14])
    #print(T[15])
    #print(T[16])
    #print(T[17])
    #print(T[18])
    #print(T[19])
    #print(T[20])
    #print(T[21])
    #print(T[22])
    #print(T[23])
    #print(T[24])
    #print(T[25])
    #print(T[26])
    #print(T[27])
    #print(T[28])
    #print(T[29])
    #print(T[30])
    #print(T[31])
    #print(T[32])
    #print(T[33])
    #print(T[34])
    #print(T[35])
    #print(T[36])
    #print(T[37])
    #print(T[38])
    #print(T[39])
    #print(T[40])
    #print(T[41])
    #print(T[42])
    #print(T[43])
    #print(T[44])
    #print(T[45])
    #print(T[46])
    #print(T[47])
    #print(T[48])
    #print(T[49])
    #print(T[50])
    #print(T[51])
    #print(T[52])
    #print(T[53])
    #print(T[54])
    #print(T[55])
    #print(T[56])
    #print(T[57])
    #print(T[58])
    #print(T[59])
    #print(T[60])
    #print(T[61])
    #print(T[62])
    #print(T[63])
    #print(T[64])

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    # print(n, k, r, s, p, t)
    # print(len(t))
    score = 0
    # for i in range(n):
    #     if t[i] == 'r':
    #         score += r
    #     elif t[i] == 's':
    #         score += s
    #     elif t[i] == 'p':
    #         score += p
    # print(score)
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                score += r
            elif t[i] == 's':
                score += s
            elif t[i] == 'p':
                score += p
        else:
            if t[i] == 'r':
                if t[i - k] == 'r':
                    score += 0
                elif t[i - k] == 's':
                    score += s
                elif t[i - k] == 'p':
                    score += p
            elif t[i] == 's':
                if t[i - k] == 'r':
                    score += r
                elif t[i - k] == 's':
                    score += 0
                elif t[i - k] == 'p':
                    score += p
            elif t[i] == 'p':
                if t[i - k] == 'r':
                    score += r
                elif t[i - k] == 's':
                    score += s
                elif t[i - k] == 'p':
                    score += 0
    print(score)

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i-k >= 0 and t[i-k] == 'r':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += p
        elif t[i] == 's':
            if i-k >= 0 and t[i-k] == 's':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += r
        elif t[i] == 'p':
            if i-k >= 0 and t[i-k] == 'p':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += s
    print(score)
