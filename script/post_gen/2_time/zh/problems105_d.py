Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    from collections import Counter
    cnt = Counter()
    for a in A:
        cnt[a % M] += 1
    ans = 0
    for c in cnt.values():
        ans += c * (c-1) // 2
    print(ans)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0 for i in range(n)]
    b[0] = a[0]%m
    for i in range(1,n):
        b[i] = (a[i]+b[i-1])%m
    c = [0 for i in range(m)]
    for i in range(n):
        c[b[i]] += 1
    ans = 0
    for i in range(m):
        ans += c[i]*(c[i]-1)//2
    ans += c[0]
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    dic = {}
    for i in range(N + 1):
        if S[i] % M in dic:
            dic[S[i] % M] += 1
        else:
            dic[S[i] % M] = 1
    ans = 0
    for i in dic:
        ans += dic[i] * (dic[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 从左到右累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 从左到右的累积和对M取余数
    for i in range(N + 1):
        S[i] %= M

    # 求每个余数的个数
    from collections import defaultdict
    dic = defaultdict(int)
    for i in range(N + 1):
        dic[S[i]] += 1

    # 求组合数
    ans = 0
    for v in dic.values():
        ans += v * (v - 1) // 2

    print(ans)

solve()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    #print(len(A))
    #print(A[1:2])
    #print(A[1:3])
    #print(A[2:3])
    #print(A[0:3])
    #print(A[0:2])
    #print(A[0:1])
    #print(A[0:0])
    #print(A[1:1])
    #print(A[2:2])
    #print(A[3:3])
    #print(A[4:4])
    #print(A[5:5])
    #print(A[6:6])
    #print(A[7:7])
    #print(A[8:8])
    #print(A[9:9])
    #print(A[10:10])
    #print(A[11:11])
    #print(A[12:12])
    #print(A[13:13])
    #print(A[14:14])
    #print(A[15:15])
    #print(A[16:16])
    #print(A[17:17])
    #print(A[18:18])
    #print(A[19:19])
    #print(A[20:20])
    #print(A[21:21])
    #print(A[22:22])
    #print(A[23:23])
    #print(A[24:24])
    #print(A[25:25])
    #print(A[26:26])
    #print(A[27:27])
    #print(A[28:28])
    #print(A[29:29])
    #print(A[30:30])
    #print(A[31:31])
    #print(A[32:32])
    #print(A[33:33])
    #print(A[34:34])
    #print(A[35:35])
    #print(A[36:36])
    #print(A[37:37])
    #print(A[38:38])
    #print(A[39:39])
    #print(A[40:40])
    #print(A[41:41])
    #print(A[42:42])
    #print(A[43:43])
    #print(A[44:44])

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i%m for i in a]
    a = [0]+a
    for i in range(1,n+1):
        a[i] += a[i-1]
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 0
    for i in d:
        ans += d[i]*(d[i]-1)//2
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] % m == 0:
            a[i] = a[i] // m
        else:
            a[i] = a[i] // m + 1
    sum = 0
    for i in range(n):
        sum += a[i]
        a[i] = sum
    a.sort()
    cnt = 1
    ans = 0
    for i in range(1,n):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    d = {}
    for x in s:
        if x%m in d:
            d[x%m] += 1
        else:
            d[x%m] = 1
    ans = 0
    for x in d:
        ans += d[x]*(d[x]-1)//2
    print(ans)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    d = {}
    for i in s:
        i %= m
        d[i] = d.get(i,0) + 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    print(ans)

=======
Suggestion 10

def main():
    #读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #计算前缀和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    #计算余数的个数
    cnt = {}
    for i in range(n + 1):
        r = s[i] % m
        if r not in cnt:
            cnt[r] = 0
        cnt[r] += 1
    #计算答案
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)
