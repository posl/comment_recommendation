Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S.append("E")
    count = 0
    for i in range(0, N):
        if S[i] == S[i+1]:
            count += 1
    count = min(count + 2 * K, N - 1)
    print(count)

=======
Suggestion 2

def cal_happy_num(str):
    happy_num = 0
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            happy_num += 1
    return happy_num

=======
Suggestion 3

def happyPeople(s):
    n = len(s)
    count = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
    return count

=======
Suggestion 4

def main():
    # 读入数据
    N, K = map(int, input().split())
    S = input()

    # 将字符串转换成列表
    S = list(S)

    # 计算最大快乐人数
    ans = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            ans += 1

    # 最多经过K次操作后可能出现的最大快乐人数
    ans += 2 * K
    print(min(ans, N - 1))

=======
Suggestion 5

def max_happy(N,K,S):
    #统计快乐人数
    happy = 0
    #统计快乐人数的最大值
    max_happy = 0
    #统计快乐人数的最大值的左端点
    max_happy_left = 0
    #统计快乐人数的最大值的右端点
    max_happy_right = 0
    #统计快乐人数的最大值的左端点
    happy_left = 0
    #统计快乐人数的最大值的右端点
    happy_right = 0
    #统计快乐人数的最大值的左端点
    happy_left_temp = 0
    #统计快乐人数的最大值的右端点
    happy_right_temp = 0
    #统计快乐人数的最大值的左端点
    happy_left_temp2 = 0
    #统计快乐人数的最大值的右端点
    happy_right_temp2 = 0
    #统计快乐人数的最大值的左端点
    happy_left_temp3 = 0
    #统计快乐人数的最大值的右端点
    happy_right_temp3 = 0
    #统计快乐人数的最大值的左端点
    happy_left_temp4 = 0
    #统计快乐人数的最大值的右端点
    happy_right_temp4 = 0
    #统计快乐人数的最大值的左端点
    happy_left_temp5 = 0
    #统计快乐人数的最大值的右端点
    happy_right_temp5 = 0
    #统计快乐人数的最大值的左端点
    happy_left_temp6 = 0
    #统计快乐人数的最大值的右端点
    happy_right_temp6 = 0
    #统计快乐人数的

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    s = input()
    happy = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            happy += 1
    print(min(happy + 2 * k, n-1))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    s = input()
    #print(n, k, s)
    #n, k = 6, 1
    #s = 'LRLRRL'
    #n, k = 13, 3
    #s = 'LRRLRLRRLLR'
    #n, k = 10, 1
    #s = 'LLLLLRRRRRR'
    #n, k = 9, 2
    #s = 'RRRLRLL'
    #n, k = 9, 1
    #s = 'RRRLRLL'
    #n, k = 9, 0
    #s = 'RRRLRLL'
    #n, k = 9, 3
    #s = 'RRRLRLL'
    #n, k = 9, 4
    #s = 'RRRLRLL'
    #n, k = 9, 5
    #s = 'RRRLRLL'
    #n, k = 9, 6
    #s = 'RRRLRLL'
    #n, k = 9, 7
    #s = 'RRRLRLL'
    #n, k = 9, 8
    #s = 'RRRLRLL'
    #n, k = 9, 9
    #s = 'RRRLRLL'
    #n, k = 9, 10
    #s = 'RRRLRLL'
    #n, k = 9, 11
    #s = 'RRRLRLL'
    #n, k = 9, 12
    #s = 'RRRLRLL'
    #n, k = 9, 13
    #s = 'RRRLRLL'
    #n, k = 9, 14
    #s = 'RRRLRLL'
    #n, k = 9, 15
    #s = 'RRRLRLL'
    #n, k = 9, 16
    #s = 'RRRLRLL'
    #n, k = 9, 17
    #s = 'RRRLRLL'
    #n, k =

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    s = input()
    happy = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            happy += 1
    happy += 2*k
    if happy > n-1:
        happy = n-1
    print(happy)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    for i in range(1, N):
        if S[i] == S[i-1]:
            count += 1
    count += 2 * K
    print(min(count, N-1))
