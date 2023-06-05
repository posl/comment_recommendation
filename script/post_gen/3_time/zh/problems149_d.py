Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    score = {'r': p, 's': r, 'p': s}
    win = {'r': 'p', 's': 'r', 'p': 's'}
    dp = [[0] * 3 for _ in range(n + 1)]
    for i in range(n):
        for j in range(3):
            if i >= k and win[t[i]] == win[t[i - k]] and j == win[t[i]]:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + score[win[t[i]]])
    print(max(dp[n]))

solve()

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i - k >= 0 and t[i-k] == 'r':
                t[i] = 'p'
            else:
                ans += p
        elif t[i] == 's':
            if i - k >= 0 and t[i-k] == 's':
                t[i] = 'r'
            else:
                ans += r
        else:
            if i - k >= 0 and t[i-k] == 'p':
                t[i] = 's'
            else:
                ans += s
    print(ans)

=======
Suggestion 3

def main():
    n,k,r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                t = t[:i] + 'x' + t[i+1:]
            else:
                score += s
    print(score)
    return 0

=======
Suggestion 4

def solve():
    # 读入数据
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    # 按照题意，玩家不能使用他/她在第（i-K）轮中使用的手。
    # 因此，我们只需要记录前K轮的手势即可。
    # 为了简化编程，我们使用一个长度为K的数组来记录前K轮的手势。
    # 由于我们只需要记录前K轮的手势，因此我们可以使用一个长度为K的滑动窗口来记录前K轮的手势。
    # 为了方便起见，我们使用一个长度为3的数组来记录前K轮的手势。
    # 该数组的第0个元素表示前K轮的手势中，石头的个数；
    # 该数组的第1个元素表示前K轮的手势中，剪刀的个数；
    # 该数组的第2个元素表示前K轮的手势中，布的个数。
    # 例如，如果前K轮的手势是{布、石头、石头、剪刀、布}，则该数组的值为{2、1、2}。
    # 为了简化编程，我们使用一个长度为3的滑动窗口来记录前K轮的手势。
    # 该滑动窗口的第0个元素表示前K轮的手势中，石头的个数；
    # 该滑动窗口的第1个元素表示前K轮的手势中，剪刀的个数；
    # 该滑动窗口的第2个元素表示前K轮的手势中，布的个数。
    # 例如，如果前K轮的手势是{布、石头、石头、剪刀、布}，

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # print(N, K, R, S, P, T)
    # print(T[0:K])
    # print(T[K:N])
    # print(T[N - K:N])
    # print(T[0:N - K])
    # print(T[K:N - K])
    # print(T[0:K] + T[N - K:N])
    # print(T[0:N - K] + T[K:N])
    # print(T[K:N] + T[0:K])
    # print(T[N - K:N] + T[0:N - K])
    # print(T[0:N - K] + T[K:N] + T[0:K])
    # print(T[K:N] + T[0:K] + T[N - K:N])
    # print(T[N - K:N] + T[0:N - K] + T[K:N])
    # print(T[0:K] + T[N - K:N] + T[K:N])
    # print(T[0:N - K] + T[K:N] + T[N - K:N])
    # print(T[K:N] + T[N - K:N] + T[0:K])
    # print(T[N - K:N] + T[0:K] + T[K:N])
    # print(T[0:K] + T[N - K:N] + T[K:N] + T[0:N - K])
    # print(T[0:N - K] + T[K:N] + T[N - K:N] + T[0:K])
    # print(T[K:N] + T[0:K] + T[N - K:N] + T[0:N - K])
    # print(T[N - K:N] + T[0:K] + T[K:N] + T[0:N - K])
    # print(T[0:N - K] + T[K:N] + T[N - K:N] + T[0:K] + T[K:N])
    # print(T[K:N] + T[0:K] + T[N - K:N] + T[0:N - K] + T[K:N])
    # print(T[N - K:N] + T[

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                t = t[:i]+'x'+t[i+1:]
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                t = t[:i]+'x'+t[i+1:]
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                t = t[:i]+'x'+t[i+1:]
            else:
                score += s
    print(score)

=======
Suggestion 7

def cal(N,K,R,S,P,T):
    sum = 0
    for i in range(N):
        if T[i] == 'r':
            if i >= K and T[i-K] == 'r':
                T[i] = 'p'
            else:
                sum += P
        elif T[i] == 's':
            if i >= K and T[i-K] == 's':
                T[i] = 'r'
            else:
                sum += R
        else:
            if i >= K and T[i-K] == 'p':
                T[i] = 's'
            else:
                sum += S
    return sum

N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
print(cal(N,K,R,S,P,T))

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                t = t[:i] + ' ' + t[i+1:]
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                t = t[:i] + ' ' + t[i+1:]
            else:
                score += r
        else:
            if i >= k and t[i-k] == 'p':
                t = t[:i] + ' ' + t[i+1:]
            else:
                score += s
    print(score)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    #print(n,k,r,s,p,t)
    #print(len(t))
    #print(t[0])
    #print(t[1])
    #print(t[2])
    #print(t[3])
    #print(t[4])
    #print(t[5])
    #print(t[6])
    #print(t[7])
    #print(t[8])
    #print(t[9])
    #print(t[10])
    #print(t[11])
    #print(t[12])
    #print(t[13])
    #print(t[14])
    #print(t[15])
    #print(t[16])
    #print(t[17])
    #print(t[18])
    #print(t[19])
    #print(t[20])
    #print(t[21])
    #print(t[22])
    #print(t[23])
    #print(t[24])
    #print(t[25])
    #print(t[26])
    #print(t[27])
    #print(t[28])
    #print(t[29])
    #print(t[30])
    #print(t[31])
    #print(t[32])
    #print(t[33])
    #print(t[34])
    #print(t[35])
    #print(t[36])
    #print(t[37])
    #print(t[38])
    #print(t[39])
    #print(t[40])
    #print(t[41])
    #print(t[42])
    #print(t[43])
    #print(t[44])
    #print(t[45])
    #print(t[46])
    #print(t[47])
    #print(t[48])
    #print(t[49])
    #print(t[50])
    #print(t[51])
    #print(t[52])
    #print(t[53])
    #print(t[54])
    #print(t[55])
    #print(t[56])
    #print(t[57])
    #print(t[58])
    #print(t[59])
    #print(t[60])
    #print(t[61])
    #print(t[62])
    #print(t[63])
    #print(t[64])

=======
Suggestion 10

def solve():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()

    #dp[i][j]表示在第i轮时，我方手势为j时的最大分数
    dp = [[0,0,0] for i in range(N+1)]
    for i in range(N):
        #我方手势为石头
        if T[i] == 'r':
            dp[i+1][0] = max(dp[i+1][0],dp[i][1]+P,dp[i][2]+P)
            dp[i+1][1] = max(dp[i+1][1],dp[i][0])
            dp[i+1][2] = max(dp[i+1][2],dp[i][0])
        #我方手势为剪刀
        if T[i] == 's':
            dp[i+1][0] = max(dp[i+1][0],dp[i][1])
            dp[i+1][1] = max(dp[i+1][1],dp[i][0]+R,dp[i][2]+R)
            dp[i+1][2] = max(dp[i+1][2],dp[i][0])
        #我方手势为布
        if T[i] == 'p':
            dp[i+1][0] = max(dp[i+1][0],dp[i][1])
            dp[i+1][1] = max(dp[i+1][1],dp[i][0])
            dp[i+1][2] = max(dp[i+1][2],dp[i][0]+S,dp[i][1]+S)

        for j in range(3):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])

        if i+1>=K:
            for j in range(3):
                for k in range(3):
                    if j!=k:
                        dp[i+1][j] = max(dp[i+1][j],dp[i-K+1][k]+dp[i+1][j])

    print(max(dp[N]))
