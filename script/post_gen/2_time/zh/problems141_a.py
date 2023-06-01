Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    ans += min(2*K, N-1)
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    s = input()
    happy = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            happy += 1
    happy += min(n - 1, 2 * k)
    print(happy)

=======
Suggestion 3

def solve(n,k,s):
    # 从左向右遍历
    # 从左向右遍历，如果是L，记录下来
    # 如果是R，如果前面有L，记录下来
    # 如果是R，如果前面没有L，记录下来
    # 如果是R，如果前面有R，不记录下来
    # 从右向左遍历
    # 从右向左遍历，如果是R，记录下来
    # 如果是L，如果前面有R，记录下来
    # 如果是L，如果前面没有R，记录下来
    # 如果是L，如果前面有L，不记录下来
    # 遍历两遍，得到两个数组，分别记录从左向右和从右向左的快乐人数
    # 如果k<=n/2，那么遍历两个数组，取出前k个最大的数，相加即可
    # 如果k>n/2，那么遍历两个数组，取出所有的数，相加即可
    # 如果k==n/2，那么遍历两个数组，取出所有的数，相加即可
    l = []
    r = []
    l.append(0)
    r.append(0)
    for i in range(n):
        if s[i] == 'L':
            l.append(i+1)
        else:
            if len(l) == 1:
                pass
            elif s[l[-1]-1] == 'L':
                l.append(i+1)
            else:
                pass
    for i in range(n-1,-1,-1):
        if s[i] == 'R':
            r.append(n-i)
        else:
            if len(r) == 1:
                pass
            elif s[n-r[-1]] == 'R':
                r.append(n-i)
            else:
                pass
    if k <= n/2:
        l.sort(reverse=True)
        r.sort(reverse=True)
        print(sum(l[:k]) + sum(r[:k]))
    else:
        print(sum(l) + sum(r))

=======
Suggestion 4

def reverse(s, l, r):
    s = list(s)
    for i in range((r-l+1)//2):
        s[l+i], s[r-i] = s[r-i], s[l+i]
    return ''.join(s)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    ans = 0
    for i in range(1, N):
        if S[i - 1] == S[i]:
            ans += 1
    ans += 2 * K
    print(min(ans, N - 1))

=======
Suggestion 6

def solve(s, k):
    n = len(s)
    # 从左到右，计算每个人在原始方向上是否快乐
    happy = [0] * n
    for i in range(1, n):
        if s[i - 1] == s[i]:
            happy[i] = 1
    # 从左到右，计算每个人在原始方向上的快乐累计值
    happy_sum = [0] * n
    happy_sum[0] = happy[0]
    for i in range(1, n):
        happy_sum[i] = happy_sum[i - 1] + happy[i]
    # 从右到左，计算每个人在反方向上是否快乐
    happy_rev = [0] * n
    for i in range(n - 2, -1, -1):
        if s[i + 1] == s[i]:
            happy_rev[i] = 1
    # 从右到左，计算每个人在反方向上的快乐累计值
    happy_rev_sum = [0] * n
    happy_rev_sum[n - 1] = happy_rev[n - 1]
    for i in range(n - 2, -1, -1):
        happy_rev_sum[i] = happy_rev_sum[i + 1] + happy_rev[i]
    # 从左到右，计算每个人经过k次操作后的快乐值
    happy_k = [0] * n
    for i in range(n):
        happy_k[i] = happy_sum[i]
        if i + k < n:
            happy_k[i] += happy_rev_sum[i + k]
    return max(happy_k)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    s = input()
    s = list(s)
    s.append(' ')
    #print(s)
    ans = 0
    for i in range(n):
        if s[i] == s[i+1]:
            ans += 1
    ans += 2 * min(k, ans)
    print(ans)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    S = input()
    #print(N,K,S)
    #print(type(N),type(K),type(S))
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
    #

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)

    # 1. 从左到右扫描，找到第一个和前面不一样的位置，记为a
    # 2. 从右到左扫描，找到第一个和前面不一样的位置，记为b
    # 3. 从a到b之间的人都是happy的
    # 4. 如果a的左边有人，那么a的左边的人都是happy的
    # 5. 如果b的右边有人，那么b的右边的人都是happy的
    # 6. 如果a的左边有人，那么a的左边的人都是happy的
    # 7. 如果b的右边有人，那么b的右边的人都是happy的
    # 8. 如果a的左边有人，那么a的左边的人都是happy的
    # 9. 如果b的右边有人，那么b的右边的人都是happy的
    # 10. 如果a的左边有人，那么a的左边的人都是happy的
    # 11. 如果b的右边有人，那么b的右边的人都是happy的
    # 12. 如果a的左边有人，那么a的左边的人都是happy的
    # 13. 如果b的右边有人，那么b的右边的人都是happy的
    # 14. 如果a的左边有人，那么a的左边的人都是happy的
    # 15. 如果b的右边有人，那么b的右边的人都是happy的
    # 16. 如果a的左边有人，那么a的左边的人都是happy的
    # 17. 如果b的右边有

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    happy += 2*K
    print(min(happy,N-1))

main()
