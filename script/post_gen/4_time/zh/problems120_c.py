Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
    print(count*2 if count*2 < len(S) else len(S))

=======
Suggestion 2

def solution():
    s = input()
    print(min(s.count('1'), s.count('0')) * 2)

solution()

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    red = [0] * (n + 1)
    blue = [0] * (n + 1)
    for i in range(n):
        red[i+1] = red[i] + (s[i] == "0")
        blue[i+1] = blue[i] + (s[i] == "1")

    ans = 0
    for i in range(n):
        ans = max(ans, red[i] + blue[n] - blue[i])

    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
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
    #print(S[67])
    #print(S[68])

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    R = S.count('0')
    B = N - R
    print(min(R, B) * 2)

=======
Suggestion 6

def solve():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N):
        if S[i] == '1':
            cnt += 1
    print(min(cnt, N-cnt)*2)

=======
Suggestion 7

def main():
    print("问题陈述")
    print("在一张桌子上有N个垂直堆放的立方体。")
    print("如果S中的第i个字符是0，则从底部开始的第i个立方体的颜色是红色，如果该字符是1，则是蓝色。")
    print("你可以进行以下任意次数的操作：选择一个相邻的红色立方体和一个蓝色立方体，然后把它们移走。在这里，堆积在被移走的立方体上的立方体将落到它们下面的物体上。")
    print("最多可以移走多少个立方体？")
    print("限制条件")
    print("1 ≦ N ≦ 10^5")
    print("|S| = N")
    print("S中的每个字符都是0或1。")
    print("输入")
    print("输入是由标准输入法提供的，其格式如下：")
    print("S")
    print("輸出")
    print("打印可移除的最大立方体数量。")
    print("样本输入1")
    print("0011")
    print("样本输出1")
    print("4")
    print("所有的四个立方体都可以被移走，操作方法如下：")
    print("从底部取出第二个和第三个立方体。然后，第四个立方体落到第一个立方体上。")
    print("从底部移走第一个和第二个立方体。")
    print("样本输入2")
    print("11011010001011")
    print("样本输出2")
    print("12")
    print("采样输入3")
    print("0")
    print("采样输出3")
    print("0")
    print("===============================================")
    print("请输入字符串：")
    s = input()
    n = len(s)
    sum = 0
    for i in range(0,n):
        if

=======
Suggestion 8

def solve(s):
    s = list(s)
    ans = 0
    while True:
        if len(s) == 0:
            break
        if s[0] == s[-1]:
            ans += 1
            s = s[1:-1]
        else:
            break
    return ans

=======
Suggestion 9

def problems120_c():
    pass

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    s = s[::-1]
    ans = 0
    cnt = 0
    for i in range(n):
        if s[i] == '0':
            cnt += 1
        else:
            ans += min(cnt, i - cnt)
    print(ans)
