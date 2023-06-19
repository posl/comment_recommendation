Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    s = set()
    for i in range(N-K+1):
        s.add(len(set(C[i:i+K])))
    print(max(s))

=======
Suggestion 2

def problems210_c():
    N,K = map(int,input().split())
    c = list(map(int,input().split()))
    c_dict = {}
    for i in range(K):
        if c[i] in c_dict:
            c_dict[c[i]] += 1
        else:
            c_dict[c[i]] = 1
    c_dict_len = len(c_dict)
    c_dict_len_max = c_dict_len
    for i in range(K,N):
        if c[i] in c_dict:
            c_dict[c[i]] += 1
        else:
            c_dict[c[i]] = 1
            c_dict_len += 1
        c_dict[c[i-K]] -= 1
        if c_dict[c[i-K]] == 0:
            c_dict_len -= 1
        if c_dict_len_max < c_dict_len:
            c_dict_len_max = c_dict_len
    print(c_dict_len_max)

problems210_c()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))

    # 1. 从左到右遍历，记录每个颜色出现的次数
    # 2. 从左到右遍历，记录每个连续K个糖果的颜色数目
    # 3. 取最大值
    color = {}
    for i in range(N):
        if c[i] in color:
            color[c[i]] += 1
        else:
            color[c[i]] = 1

    # print(color)
    max_color = max(color.values())
    # print(max_color)

    color = {}
    for i in range(K):
        if c[i] in color:
            color[c[i]] += 1
        else:
            color[c[i]] = 1

    # print(color)
    max_color = max(max_color, len(color))
    # print(max_color)

    for i in range(K, N):
        if c[i-K] in color:
            color[c[i-K]] -= 1
            if color[c[i-K]] == 0:
                del color[c[i-K]]
        if c[i] in color:
            color[c[i]] += 1
        else:
            color[c[i]] = 1
        # print(color)
        max_color = max(max_color, len(color))
        # print(max_color)

    print(max_color)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        d[c[i]] = 1
    ans = len(d)
    for i in range(k, n):
        d[c[i]] = 1
        d[c[i-k]] -= 1
        if d[c[i-k]] == 0:
            del d[c[i-k]]
        ans = max(ans, len(d))
    print(ans)

=======
Suggestion 5

def main():
    # 读取输入
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    # 求解
    ans = 0
    s = set()
    for i in range(n-k+1):
        for j in range(k):
            s.add(c[i+j])
        ans = max(ans, len(s))
        s.clear()

    # 输出
    print(ans)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    c = list(map(int,input().split()))
    #print(N,K,c)
    #print(len(c))
    #print(c[0])
    #print(c[1])
    #print(c[2])
    #print(c[3])
    #print(c[4])
    #print(c[5])
    #print(c[6])
    #print(c[7])
    #print(c[8])
    #print(c[9])
    #print(c[10])
    #print(c[11])
    #print(c[12])
    #print(c[13])
    #print(c[14])
    #print(c[15])
    #print(c[16])
    #print(c[17])
    #print(c[18])
    #print(c[19])
    #print(c[20])
    #print(c[21])
    #print(c[22])
    #print(c[23])
    #print(c[24])
    #print(c[25])
    #print(c[26])
    #print(c[27])
    #print(c[28])
    #print(c[29])
    #print(c[30])
    #print(c[31])
    #print(c[32])
    #print(c[33])
    #print(c[34])
    #print(c[35])
    #print(c[36])
    #print(c[37])
    #print(c[38])
    #print(c[39])
    #print(c[40])
    #print(c[41])
    #print(c[42])
    #print(c[43])
    #print(c[44])
    #print(c[45])
    #print(c[46])
    #print(c[47])
    #print(c[48])
    #print(c[49])
    #print(c[50])
    #print(c[51])
    #print(c[52])
    #print(c[53])
    #print(c[54])
    #print(c[55])
    #print(c[56])
    #print(c[57])
    #print(c[58])
    #print(c[59])
    #print(c[60])
    #print(c[61])
    #print(c[62])
    #print(c[63])
    #print(c[64])
    #print(c[65])
    #print

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    kind = 0
    color = [0]*(10**9+1)
    for i in range(k):
        if color[c[i]] == 0:
            kind += 1
        color[c[i]] += 1
    ans = kind
    for i in range(k,n):
        if color[c[i]] == 0:
            kind += 1
        color[c[i]] += 1
        color[c[i-k]] -= 1
        if color[c[i-k]] == 0:
            kind -= 1
        ans = max(ans,kind)
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    max_kinds = 0
    for i in range(n-k+1):
        kinds = len(set(candies[i:i+k]))
        if kinds > max_kinds:
            max_kinds = kinds
    print(max_kinds)

=======
Suggestion 9

def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    if n <= k:
        print(len(set(c)))
        return

    d = dict()
    for i in range(k):
        if c[i] in d:
            d[c[i]] += 1
        else:
            d[c[i]] = 1

    ans = len(d)
    for i in range(n - k):
        if c[i] in d:
            d[c[i]] -= 1
            if d[c[i]] == 0:
                del d[c[i]]

        if c[i + k] in d:
            d[c[i + k]] += 1
        else:
            d[c[i + k]] = 1

        ans = max(ans, len(d))

    print(ans)

=======
Suggestion 10

def main():
    n,k=map(int,input().split())
    candy=list(map(int,input().split()))
    candy_set=set(candy)
    candy_set_len=len(candy_set)
    if candy_set_len<k:
        print(candy_set_len)
        return
    candy_dict={}
    for i in range(k):
        if candy[i] not in candy_dict:
            candy_dict[candy[i]]=1
        else:
            candy_dict[candy[i]]+=1
    max_len=len(candy_dict)
    for i in range(k,n):
        candy_dict[candy[i-k]]-=1
        if candy_dict[candy[i-k]]==0:
            del candy_dict[candy[i-k]]
        if candy[i] not in candy_dict:
            candy_dict[candy[i]]=1
        else:
            candy_dict[candy[i]]+=1
        if max_len<len(candy_dict):
            max_len=len(candy_dict)
    print(max_len)
