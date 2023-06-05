Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    # print(n,m,a)
    # print(type(n),type(m),type

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = ""
    while N > 0:
        for i in range(M):
            if N >= A[i]:
                ans += str(A[i])
                N -= A[i]
                break
    print(ans)

=======
Suggestion 3

def main():
    #输入
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    #预处理
    #将数字和其对应的火柴棒数量存储在字典中
    a_dict = {}
    for i in range(m):
        a_dict[a_list[i]] = i + 1
    #将数字按照火柴棒数量排序
    a_list.sort(key=lambda x: a_dict[x], reverse=True)
    #计算数字最大长度
    max_len = n // a_dict[a_list[-1]]
    #逐位计算
    result = ''
    for i in range(max_len, 0, -1):
        for j in range(m):
            if n - a_dict[a_list[j]] == 0:
                result += str(a_list[j])
                n -= a_dict[a_list[j]]
                break
            elif n - a_dict[a_list[j]] < 0:
                continue
            elif n - a_dict[a_list[j]] > 0:
                result += str(a_list[j])
                n -= a_dict[a_list[j]]
                break
    #输出
    print(result)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    nums = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] == -1:
            continue
        for j in range(len(a)):
            if i + nums[a[j] - 1] <= n:
                dp[i + nums[a[j] - 1]] = max(dp[i + nums[a[j] - 1]], dp[i] * 10 + a[j])
    print(dp[n])

=======
Suggestion 5

def get_max_num(n, a_list):
    a_list.sort(reverse=True)
    num = 0
    for i in a_list:
        num += i * 10**(i-1)
    return num

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, m, a)
    l = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    a = [l[i-1] for i in a]
    #print(a)
    dp = [0] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(m):
            if i >= a[j]:
                dp[i] = max(dp[i], dp[i-a[j]]*10+j+1)
    print(dp[n])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    num = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for j in range(M):
            if i - num[A[j]-1] >= 0:
                dp[i] = max(dp[i], dp[i-num[A[j]-1]]*10+A[j])
    print(dp[N])

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0 for i in range(n + 1)]
    for i in range(m):
        for j in range(a[i], n + 1):
            dp[j] = max(dp[j], dp[j - a[i]] * 10 + a[i])
    print(dp[n])

=======
Suggestion 9

def get_max_number(n, m, a_list):
    # a_list.sort(reverse=True)
    # print(a_list)
    # print(n, m)
    # print(a_list)
    # a_list.sort(reverse=True)
    # print(a_list)
    # print(a_list[0])
    # print(a_list[1])
    # print(a_list[2])
    # print(a_list[3])
    # print(a_list[4])
    # print(a_list[5])
    # print(a_list[6])
    # print(a_list[7])
    # print(a_list[8])
    # print(a_list[9])
    # print(a_list[10])
    # print(a_list[11])
    # print(a_list[12])
    # print(a_list[13])
    # print(a_list[14])
    # print(a_list[15])
    # print(a_list[16])
    # print(a_list[17])
    # print(a_list[18])
    # print(a_list[19])
    # print(a_list[20])
    # print(a_list[21])
    # print(a_list[22])
    # print(a_list[23])
    # print(a_list[24])
    # print(a_list[25])
    # print(a_list[26])
    # print(a_list[27])
    # print(a_list[28])
    # print(a_list[29])
    # print(a_list[30])
    # print(a_list[31])
    # print(a_list[32])
    # print(a_list[33])
    # print(a_list[34])
    # print(a_list[35])
    # print(a_list[36])
    # print(a_list[37])
    # print(a_list[38])
    # print(a_list[39])
    # print(a_list[40])
    # print(a_list[41])
    # print(a_list[42])
    # print(a_list[43])
    # print(a_list[44])
    # print(a_list[45])
    # print(a_list[46])
    # print(a_list[47])
    # print(a_list[48])
    # print(a_list[49])
    # print(a_list[50])
    # print(a_list[51])
    # print(a_list[52])
    # print(a_list[53])
    # print(a_list[54])
    # print(a_list[55])

=======
Suggestion 10

def solve(n, m, a):
    # 1. 从大到小排序
    # 2. 从大到小排列的数字拼接起来
    # 3. 从大到小排列的数字拼接起来后，如果大于n，则去掉最后一个数字，再判断
    # 4. 如果小于n，则去掉最后一个数字，再判断
    # 5. 如果等于n，则直接返回

    # 1. 从大到小排序
    a.sort(reverse=True)

    # 2. 从大到小排列的数字拼接起来
    num = ''
    for i in range(m):
        num += str(a[i])

    # 3. 从大到小排列的数字拼接起来后，如果大于n，则去掉最后一个数字，再判断
    while int(num) > n:
        num = num[:-1]

    # 4. 如果小于n，则去掉最后一个数字，再判断
    while int(num) < n:
        num = num[:-1]

    # 5. 如果等于n，则直接返回
    return num

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
