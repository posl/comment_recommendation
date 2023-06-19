Synthesizing 10/10 solutions

=======
Suggestion 1

def findMaxNum(n,m,a):
    #找出正好可以用N根火柴棒组成的最大的整数
    #整数中的每个数字必须是数字A_1, A_2, ..., A_M（1 ≦ A_i ≦ 9）中的一个。
    #用来组成数字1，2，3，4，5，6，7，8，9的火柴棒数量应该分别为2，5，5，4，5，6，3，7，6。
    #限制条件
    #输入的所有数值都是整数。
    #2 ≦ N ≦ 10^4
    #1 ≦ M ≦ 9
    #1 ≦ A_i ≦ 9
    #A_i都是不同的。
    #存在一个整数，在条件下正好可以由N个火柴棒组成。
    #输入
    #输入是由标准输入法提供的，其格式如下：
    #N M
    #A_1 A_2 ...A_M
    #输出
    #打印在问题陈述的条件下，用N根火柴棍所能形成的最大整数。
    #输入样本 1
    #20 4
    #3 7 8 4
    #样本输出1
    #777773
    #整数77773可以用3+3+3+3+3+5=20根火柴棒组成，这是在条件下20根火柴棒可以组成的最大整数。
    #输入样本2
    #101 9
    #9 8 7 6 5 4 3 2 1
    #样本输出2
    #711

=======
Suggestion 2

def solve(N, M, A):
    # dp[i]表示用i根火柴棍所能形成的最大整数
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(M):
            if i >= A[j] and dp[i - A[j]] != -1:
                dp[i] = max(dp[i], dp[i - A[j]] * 10 + j + 1)
    return dp[N]

=======
Suggestion 3

def find_max_num(n, m, a):
    a.sort()
    a.reverse()
    #print a
    max_num = 0
    max_num_list = []
    for i in range(0, m):
        if n > a[i]:
            max_num_list.append(a[i])
            n = n - a[i]
        elif n == a[i]:
            max_num_list.append(a[i])
            break
        else:
            continue
    #print max_num_list

    for j in range(0, len(max_num_list)):
        max_num = max_num * 10 + max_num_list[j]
    return max_num

=======
Suggestion 4

def main():
    n,m = map(int,raw_input().split())
    a = map(int,raw_input().split())
    a.sort()
    a.reverse()
    #print a
    num = []
    for i in range(m):
        if i == 0:
            for j in range(a[i]):
                num.append(i+1)
        else:
            for j in range(a[i]-a[i-1]):
                num.append(i+1)
    #print num
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(num[0])
        else:
            ans.append(num[i%len(num)])
    #print ans
    for i in range(len(ans)):
        print ans[i],
    print ''

=======
Suggestion 5

def main():
    # 输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 全排列
    a.sort(reverse=True)
    # 从最大的数字开始，每次减去一个数字，直到数字用完
    ans = []
    while n > 0:
        for i in range(m):
            if n - a[i] >= 0:
                ans.append(a[i])
                n -= a[i]
                break

    # 输出
    for i in range(len(ans)):
        print(ans[i], end='')

=======
Suggestion 6

def get_max_number(n, m, a):
    # 用来组成数字1，2，3，4，5，6，7，8，9的火柴棒数量
    match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    match_dict = {}
    for i in range(m):
        match_dict[a[i]] = match[i]

    # 定义dp数组，dp[i]表示用i根火柴棒能组成的最大整数
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i >= match_dict[a[j]] and dp[i - match_dict[a[j]]] != -1:
                dp[i] = max(dp[i], dp[i - match_dict[a[j]]] * 10 + int(a[j]))

    return dp[n]

=======
Suggestion 7

def find_max_num(n, m, a):
    # 1. 选出最小的数字
    # 2. 从大到小排列
    # 3. 从最大的数字开始，选出最大的数字
    # 4. 重复3，直到火柴棒用完
    # 5. 如果火柴棒用完，但是数字没有选完，那么从头开始选

    # 1. 选出最小的数字
    min_num = 9
    for i in range(m):
        if a[i] < min_num:
            min_num = a[i]
    print('min_num:', min_num)

    # 2. 从大到小排列
    a.sort(reverse=True)
    print('a:', a)

    # 3. 从最大的数字开始，选出最大的数字
    num = ''
    while n > 0:
        for i in range(m):
            if a[i] <= n:
                num = num + str(a[i])
                n = n - a[i]
                break
    print('num:', num)

    # 5. 如果火柴棒用完，但是数字没有选完，那么从头开始选
    if n == 0:
        return num
    else:
        return find_max_num(n, m, a)

=======
Suggestion 8

def get_max_num(N, M, A):
    Max = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    A.sort(reverse=True)
    #print(A)
    dp = [-1 for i in range(N+1)]
    dp[0] = 0
    for i in range(N+1):
        for j in range(M):
            if i-Max[A[j]-1] >= 0 and dp[i-Max[A[j]-1]] != -1:
                dp[i] = max(dp[i], dp[i-Max[A[j]-1]]+1)
    #print(dp)
    num = []
    if dp[N] == -1:
        return -1
    while N > 0:
        for i in range(M):
            if N >= Max[A[i]-1] and dp[N-Max[A[i]-1]] == dp[N]-1:
                num.append(A[i])
                N -= Max[A[i]-1]
                break
    num.sort(reverse=True)
    return num

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    #print(A[0], A[1], A[2])
    #print(A[0]+A[1]+A[2])
    #print(A[0]+A[1]+A[2]+A[0])
    #print(A[0]+A[1]+A[2]+A[0]+A[1])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0])
    #print(A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1]+A[2]+A[0]+A[1])
    #print(A[0]+

=======
Suggestion 10

def max_num(n, m, a):
    #a.sort(reverse=True)
    #print(a)
    #print(n)
    #print(m)
    #print(a)
    #print(len(a))
    #print(a[0])
    #print(a[1])
    #print(a[2])
    #print(a[3])
    #print(a[4])
    #print(a[5])
    #print(a[6])
    #print(a[7])
    #print(a[8])
    #print(a[9])
    #print(a[10])
    #print(a[11])
    #print(a[12])
    #print(a[13])
    #print(a[14])
    #print(a[15])
    #print(a[16])
    #print(a[17])
    #print(a[18])
    #print(a[19])
    #print(a[20])
    #print(a[21])
    #print(a[22])
    #print(a[23])
    #print(a[24])
    #print(a[25])
    #print(a[26])
    #print(a[27])
    #print(a[28])
    #print(a[29])
    #print(a[30])
    #print(a[31])
    #print(a[32])
    #print(a[33])
    #print(a[34])
    #print(a[35])
    #print(a[36])
    #print(a[37])
    #print(a[38])
    #print(a[39])
    #print(a[40])
    #print(a[41])
    #print(a[42])
    #print(a[43])
    #print(a[44])
    #print(a[45])
    #print(a[46])
    #print(a[47])
    #print(a[48])
    #print(a[49])
    #print(a[50])
    #print(a[51])
    #print(a[52])
    #print(a[53])
    #print(a[54])
    #print(a[55])
    #print(a[56])
    #print(a[57])
    #print(a[58])
    #print(a[59])
    #print(a[60])
    #print(a[61])
    #print(a[62])
    #print(a[63])
    #print(a[64])
    #print(a
