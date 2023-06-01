Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 用来组成数字1，2，3，4，5，6，7，8，9的火柴棒数量
    B = [2, 5, 5, 4, 5, 6, 3, 7, 6]

    # 从大到小排序
    A.sort(reverse=True)
    # 从小到大排序
    # A.sort()

    # dp[i]表示用i根火柴棒所能形成的最大整数
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i >= B[A[j] - 1] and dp[i - B[A[j] - 1]] != -1:
                dp[i] = max(dp[i], dp[i - B[A[j] - 1]] * 10 + A[j])

    print(dp[N])

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i-a[j]>=0 and dp[i-a[j]]!=-1:
                dp[i] = max(dp[i],dp[i-a[j]]*10+j+1)
    print(dp[n])

=======
Suggestion 3

def max_num(n, m, a):
    # print(n, m, a)
    # print(len(a))
    # print(a)
    # print(a[0])
    # print(a[1])
    # print(a[2])
    # print(a[3])
    # print(a[4])
    # print(a[5])
    # print(a[6])
    # print(a[7])
    # print(a[8])
    # print(a[9])
    # print(a[10])
    # print(a[11])
    # print(a[12])
    # print(a[13])
    # print(a[14])
    # print(a[15])
    # print(a[16])
    # print(a[17])
    # print(a[18])
    # print(a[19])
    # print(a[20])
    # print(a[21])
    # print(a[22])
    # print(a[23])
    # print(a[24])
    # print(a[25])
    # print(a[26])
    # print(a[27])
    # print(a[28])
    # print(a[29])
    # print(a[30])
    # print(a[31])
    # print(a[32])
    # print(a[33])
    # print(a[34])
    # print(a[35])
    # print(a[36])
    # print(a[37])
    # print(a[38])
    # print(a[39])
    # print(a[40])
    # print(a[41])
    # print(a[42])
    # print(a[43])
    # print(a[44])
    # print(a[45])
    # print(a[46])
    # print(a[47])
    # print(a[48])
    # print(a[49])
    # print(a[50])
    # print(a[51])
    # print(a[52])
    # print(a[53])
    # print(a[54])
    # print(a[55])
    # print(a[56])
    # print(a[57])
    # print(a[58])
    # print(a[59])
    # print(a[60])
    # print(a[61])
    # print(a[62])
    # print(a[63])
    # print(a[64])
    # print(a[65])
    # print(a[66])
    # print

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i-a[j]>=0 and dp[i-a[j]]!=-1:
                dp[i] = max(dp[i],dp[i-a[j]]*10+a[j])
    print(dp[n])

=======
Suggestion 5

def get_max_num(n, a):
    a.sort(reverse=True)
    num = ''
    for i in a:
        while n >= i:
            num += str(i)
            n -= i
    return num

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n + 1):
            if j >= a[i]:
                dp[j] = max(dp[j], dp[j - a[i]] * 10 + a[i])
    print(dp[n])

=======
Suggestion 7

def main():
    num, match = map(int, input().split())
    matchsticks = list(map(int, input().split()))
    matchsticks.sort(reverse=True)
    dp = [-1 for _ in range(num + 1)]
    dp[0] = 0
    for i in range(1, num + 1):
        for j in range(match):
            if i >= matchsticks[j] and dp[i - matchsticks[j]] >= 0:
                dp[i] = max(dp[i], dp[i - matchsticks[j]] + 1)
    if dp[num] == -1:
        print(0)
    else:
        ans = ''
        for i in range(dp[num]):
            for j in range(match):
                if num >= matchsticks[j] and dp[num - matchsticks[j]] == dp[num] - 1:
                    ans += str(matchsticks[j])
                    num -= matchsticks[j]
                    break
        print(ans)

=======
Suggestion 8

def max_number(n, m, a):
    # 从大到小排序
    a.sort(reverse=True)
    # 从大到小拼接
    result = ''
    while n > 0:
        for i in range(m):
            if n >= a[i]:
                result += str(a[i])
                n -= a[i]
                break
    return result

=======
Suggestion 9

def findMaxNum(N, M, A):
    # print(N, M, A)
    # print(A)
    # print(len(A))
    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])

    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])

    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])

    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])

    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])

    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])

    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    # print(A[5])
    # print(A[6])
    # print(A[7])
    # print(A[8])

    # print(A[0])
    # print(A[1])
    # print(A[2])
    # print(A[3])
    # print(A[4])
    #
