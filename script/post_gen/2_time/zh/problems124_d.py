Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    s = input()
    # print(n, k, s)
    # print(s[0])
    # print(s[1])
    # print(s[2])
    # print(s[3])
    # print(s[4])
    # print(s[5])
    # print(s[6])
    # print(s[7])
    # print(s[8])
    # print(s[9])
    # print(s[10])
    # print(s[11])
    # print(s[12])
    # print(s[13])
    # print(s[14])
    # print(s[15])
    # print(s[16])
    # print(s[17])
    # print(s[18])
    # print(s[19])
    # print(s[20])
    # print(s[21])
    # print(s[22])
    # print(s[23])
    # print(s[24])
    # print(s[25])
    # print(s[26])
    # print(s[27])
    # print(s[28])
    # print(s[29])
    # print(s[30])
    # print(s[31])
    # print(s[32])
    # print(s[33])
    # print(s[34])
    # print(s[35])
    # print(s[36])
    # print(s[37])
    # print(s[38])
    # print(s[39])
    # print(s[40])
    # print(s[41])
    # print(s[42])
    # print(s[43])
    # print(s[44])
    # print(s[45])
    # print(s[46])
    # print(s[47])
    # print(s[48])
    # print(s[49])
    # print(s[50])
    # print(s[51])
    # print(s[52])
    # print(s[53])
    # print(s[54])
    # print(s[55])
    # print(s[56])
    # print(s[57])
    # print(s[58])
    # print(s[59])
    # print(s[60])
    # print(s[61])
    # print(s[62])
    # print(s[63])
    # print(s[64])
    # print(s[65])
    # print(s[66])
    # print

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    s = input()
    #print(n, k, s)
    #n, k, s = 14, 2, "11101010110011"
    #n, k, s = 5, 1, "00010"
    #n, k, s = 1, 1, "1"
    #n, k, s = 5, 1, "00010"
    #n, k, s = 5, 2, "00010"
    #n, k, s = 5, 3, "00010"
    #n, k, s = 5, 4, "00010"
    #n, k, s = 5, 5, "00010"
    #n, k, s = 5, 6, "00010"
    #n, k, s = 5, 7, "00010"
    #n, k, s = 5, 8, "00010"
    #n, k, s = 5, 9, "00010"
    #n, k, s = 5, 10, "00010"
    #n, k, s = 5, 11, "00010"
    #n, k, s = 5, 12, "00010"
    #n, k, s = 5, 13, "00010"
    #n, k, s = 5, 14, "00010"
    #n, k, s = 5, 15, "00010"
    #n, k, s = 5, 16, "00010"
    #n, k, s = 5, 17, "00010"
    #n, k, s = 5, 18, "00010"
    #n, k, s = 5, 19, "00010"
    #n, k, s = 5, 20, "00010"
    #n, k, s = 5, 21, "00010"
    #n, k, s = 5, 22, "00010"
    #n, k, s = 5, 23, "00010"
    #

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    S = input()
    ans = 0
    for i in range(1,N):
        if S[i-1] != S[i]:
            ans += 1
    ans = min(ans+2*K,N-1)
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    S = input()
    #print(N,K,S)
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #print(S[66])

=======
Suggestion 5

def main():
    # 读取输入
    n, k = map(int, input().split())
    s = input()
    # 初始化
    ans = 0
    # 从左到右遍历
    for i in range(n):
        # 如果当前是脚
        if s[i] == '0':
            # 如果是第一个
            if i == 0:
                # 如果后面是脚
                if s[i + 1] == '0':
                    # 翻转
                    ans += 1
            # 如果是最后一个
            elif i == n - 1:
                # 如果前面是脚
                if s[i - 1] == '0':
                    # 翻转
                    ans += 1
            # 如果是中间的
            else:
                # 如果前后都是脚
                if s[i - 1] == '0' and s[i + 1] == '0':
                    # 翻转
                    ans += 1
    # 如果翻转次数够
    if k <= ans:
        # 直接输出
        print(n)
        return
    # 如果翻转次数不够
    else:
        # 减去翻转次数
        ans = n - k
        # 输出
        print(ans)
        return

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def problems124_d():
    pass

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    s = input()
    
    # 从左到右计数
    left = [0] * (n+1)
    for i in range(n):
        left[i+1] = left[i] + (s[i] == '0')
    # 从右到左计数
    right = [0] * (n+1)
    for i in range(n-1,-1,-1):
        right[i] = right[i+1] + (s[i] == '1')
    
    ans = 0
    # 选择左端点
    for i in range(n+1):
        # 选择右端点
        j = min(n,i+k*2)
        # 选择左端点为i，右端点为j时，最多能有多少个人
        ans = max(ans,left[i] + right[j])
    
    print(ans)

=======
Suggestion 9

def main():
    # 读入数据
    n, k = map(int, input().split())
    s = input()

    # 从左到右，将连续的0或1的数量记录到列表中
    cnt = []
    now = s[0]
    num = 1
    for i in range(1, n):
        if s[i] == now:
            num += 1
        else:
            cnt.append(num)
            now = s[i]
            num = 1
    cnt.append(num)

    # 从左到右，将连续的0或1的数量记录到列表中
    cnt = []
    now = s[0]
    num = 1
    for i in range(1, n):
        if s[i] == now:
            num += 1
        else:
            cnt.append(num)
            now = s[i]
            num = 1
    cnt.append(num)

    # 如果第一个是0，那么第一个0之前和最后一个0之后的1都可以被翻转
    if s[0] == "0":
        ans = sum(cnt[:2 * k + 1])
    # 如果第一个是1，那么第一个1之前和最后一个1之后的0都可以被翻转
    else:
        ans = sum(cnt[:2 * k + 2])

    # 从第二个开始，每两个数之间的间隔都可以被翻转
    for i in range(1, len(cnt) - 2 * k):
        ans = max(ans, sum(cnt[i:i + 2 * k + 1]))

    # 如果最后一个是0，那么最后一个0之前和最后一个0之后的1都可以被翻转
    if s[-1] == "0":
        ans = max(ans, sum(cnt[-2 * k - 1:]))
    # 如果最后一个是1，那么最后一个1之前和最后一个1之后的0都可以被翻转
    else:
        ans = max(ans, sum(cnt[-2 * k - 2:]))

    print(ans)
