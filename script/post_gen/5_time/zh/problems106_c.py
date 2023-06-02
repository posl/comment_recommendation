Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    l = len(s)
    if l == 1:
        print(s)
    elif l == 2:
        if k == 1:
            print(s[0])
        else:
            print(s[1])
    else:
        for i in range(k):
            if s[i] != '1':
                print(s[i])
                break
            elif i == k-1:
                print('1')

=======
Suggestion 2

def func(s,k):
    #print(s,k)
    if k <= len(s):
        return s[k-1]
    else:
        return func(s,k//len(s))

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    #print(S)
    #print(K)
    count = 0
    for i in range(len(S)):
        if S[i] == '1':
            count += 1
        else:
            break
    if K <= count:
        print(1)
        return
    else:
        print(S[count-1])
        return

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    n = len(S)
    #print(n)
    #print(K)
    #print(S)
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
    #print(S

=======
Suggestion 5

def solve():
    s = input()
    k = int(input())
    size = len(s)
    if k <= size:
        print(s[k-1])
        return
    i = 0
    while i < size:
        if s[i] == '1':
            i += 1
            continue
        j = i
        while j < size and s[j] == s[i]:
            j += 1
        if j - i >= k:
            print(s[i])
            return
        k -= j - i
        i = j
    print(1)

=======
Suggestion 6

def main():
    # 读入字符串
    s = input()
    # 读入整数
    k = int(input())
    
    # 计算
    # 1.找到最终字符串的长度
    # 2.找到最终字符串的第k个字符
    # 3.输出结果
    # 1.找到最终字符串的长度
    # 1.1 首先找到原始字符串的长度
    # 1.2 然后找到最终字符串的长度
    # 1.3 最终字符串的长度 = 最终字符串的长度 - 原始字符串的长度
    # 1.4 最终字符串的长度 = 最终字符串的长度 % 9
    # 1.5 最终字符串的长度 = 最终字符串的长度 + 原始字符串的长度
    # 2.找到最终字符串的第k个字符
    # 2.1 最终字符串的第k个字符 = 原始字符串的第k个字符
    # 2.2 如果最终字符串的第k个字符是1，那么最终字符串的第k个字符 = 1
    # 2.3 如果最终字符串的第k个字符是2，那么最终字符串的第k个字符 = 2
    # 2.4 如果最终字符串的第k个字符是3，那么最终字符串的第k个字符 = 3
    # 2.5 如果最终字符串的第k个字符是4，那么最终字符串的第k个字符 = 4
    # 2.6 如果最终字符串的第k个字符是5，那么最终字符串的第k个字符 = 5
    # 2.7 如果最终字符串的第k个字符是6，那么最终字符串的第k个字符 = 6
    # 2.8 如果最终字符串的第k个字符是7，那么最终字符串的第k个字符 = 7
    # 2.9 如果

=======
Suggestion 7

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            break
    else:
        print('1')

=======
Suggestion 8

def getNum(s):
    s = s.replace('2','22')
    s = s.replace('3','333')
    s = s.replace('4','4444')
    s = s.replace('5','55555')
    s = s.replace('6','666666')
    s = s.replace('7','7777777')
    s = s.replace('8','88888888')
    s = s.replace('9','999999999')
    return s

s = input()
k = int(input())
while k > len(s):
    s = getNum(s)
print(s[k-1])

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] != "1":
            print(S[i])
            return
    print("1")
