Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_sum(arr, m):
    max_sum = 0
    for i in range(len(arr)-m+1):
        max_sum = max(max_sum, sum([arr[j]*(j+1) for j in range(i, i+m)]))
    return max_sum

=======
Suggestion 2

def get_max_sum(n, m, a):
    # 先计算出每个元素的贡献
    # 用一个数组保存，数组的每个元素表示以该元素为结尾的子数组的最大值
    # 递推公式为：f[i] = max(f[i-1] + i*a[i], i*a[i])
    # 由于f[i]只与f[i-1]相关，因此可以用一个变量来保存
    # 递推公式为：f = max(f + i*a[i], i*a[i])
    f = 0
    for i in range(m):
        f += (i+1) * a[i]
    res = f
    for i in range(m, n):
        f = max(f + (i+1) * a[i] - i * a[i-m], (i+1) * a[i])
        res = max(res, f)
    return res

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = b[i] + a[i]
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = c[i] + i * a[i]
    d = [0] * (n + 1)
    for i in range(n):
        d[i + 1] = d[i] + a[i] * (i + 1) * (n - i)
    ans = 0
    for i in range(m, n + 1):
        ans = max(ans, b[i] * i - (c[i] - c[i - m]) - (d[n] - d[i]))
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = -10**18
    for i in range(m + 1):
        for j in range(m + 1 - i):
            if i + 2 * j > m:
                continue
            t = s[i] + (s[n] - s[n - j]) + (s[n - j] - s[n - j - i])
            ans = max(ans, t)
    print(ans)
main()

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,m,a)
    #print(a)
    #print("a[0]:",a[0])
    #print("a[1]:",a[1])
    #print("a[2]:",a[2])
    #print("a[3]:",a[3])
    #print("a[4]:",a[4])
    #print("a[5]:",a[5])
    #print("a[6]:",a[6])
    #print("a[7]:",a[7])
    #print("a[8]:",a[8])
    #print("a[9]:",a[9])
    #print("a[10]:",a[10])
    #print("a[11]:",a[11])
    #print("a[12]:",a[12])
    #print("a[13]:",a[13])
    #print("a[14]:",a[14])
    #print("a[15]:",a[15])
    #print("a[16]:",a[16])
    #print("a[17]:",a[17])
    #print("a[18]:",a[18])
    #print("a[19]:",a[19])
    #print("a[20]:",a[20])
    #print("a[21]:",a[21])
    #print("a[22]:",a[22])
    #print("a[23]:",a[23])
    #print("a[24]:",a[24])
    #print("a[25]:",a[25])
    #print("a[26]:",a[26])
    #print("a[27]:",a[27])
    #print("a[28]:",a[28])
    #print("a[29]:",a[29])
    #print("a[30]:",a[30])
    #print("a[31]:",a[31])
    #print("a[32]:",a[32])
    #print("a[33]:",a[33])
    #print("a[34]:",a[34])
    #print("a[35]:",a[

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[-1] + a[i])
    from collections import deque
    q = deque()
    q.append((0, 0))
    ans = -10**18
    for i in range(1, n + 1):
        while q[0][0] < i - m:
            q.popleft()
        ans = max(ans, s[i] - q[0][1])
        while q and q[-1][1] >= s[i]:
            q.pop()
        q.append((i, s[i]))
    print(ans)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,M,A)

    #累计和
    cumsum = [0]
    for i in range(0,N):
        cumsum.append(cumsum[i]+A[i])
    #print(cumsum)

    #最大值
    maxsum = -10000000000
    for i in range(0,N-M+1):
        #print(cumsum[i+M]-cumsum[i])
        if cumsum[i+M]-cumsum[i] > maxsum:
            maxsum = cumsum[i+M]-cumsum[i]
    print(maxsum)

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    # print(n,m,a)
    # print(a)
    # for i in range(n):
    #     print(a[i])
    # for i in range(n):
    #     print(a[i], end=' ')
    #     print(a[i], end=' ')
    # print()
    # print(a)
    # print(a[0],a[1])
    # print(a[1],a[2])
    # print(a[2],a[3])
    # print(a[3],a[4])
    # print(a[4],a[5])
    # print(a[5],a[6])
    # print(a[6],a[7])
    # print(a[7],a[8])
    # print(a[8],a[9])
    # print(a[9],a[10])
    # print(a[10],a[11])
    # print(a[11],a[12])
    # print(a[12],a[13])
    # print(a[13],a[14])
    # print(a[14],a[15])
    # print(a[15],a[16])
    # print(a[16],a[17])
    # print(a[17],a[18])
    # print(a[18],a[19])
    # print(a[19],a[20])
    # print(a[20],a[21])
    # print(a[21],a[22])
    # print(a[22],a[23])
    # print(a[23],a[24])
    # print(a[24],a[25])
    # print(a[25],a[26])
    # print(a[26],a[27])
    # print(a[27],a[28])
    # print(a[28],a[29])
    # print(a[29],a[30])
    # print(a[30],a[31])
    # print(a[31],a[32])
    # print(a[32],a[33])
    # print(a[33],a[34])
    # print(a[34],a[35])
    # print(a[35],a[36])
    # print(a[36],a[37])
    # print(a[

=======
Suggestion 10

def get_input():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    return n,m,a
