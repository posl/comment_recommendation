Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(

=======
Suggestion 2

def cumsum(a):
    s = 0
    res = []
    for i in range(len(a)):
        s += a[i]
        res.append(s)
    return res

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    dic = {}
    for s in S:
        r = s % M
        if r in dic:
            dic[r] += 1
        else:
            dic[r] = 1
    ans = 0
    for v in dic.values():
        ans += v * (v - 1) // 2
    print(ans)

solve()

=======
Suggestion 4

def solve(n,m,alist):
    #alist的前缀和
    sumalist = [0]
    for i in range(n):
        sumalist.append(sumalist[i]+alist[i])
    #print(sumalist)

    #alist的前缀和的模m的余数
    modlist = [0]
    for i in range(n):
        modlist.append(sumalist[i+1]%m)
    #print(modlist)

    #modlist中的模m的余数的次数统计
    moddict = {}
    for i in modlist:
        if i in moddict:
            moddict[i] += 1
        else:
            moddict[i] = 1
    #print(moddict)

    #moddict的value中的模m的余数的次数统计
    moddict2 = {}
    for i in moddict.values():
        if i in moddict2:
            moddict2[i] += 1
        else:
            moddict2[i] = 1
    #print(moddict2)

    #moddict2中的模m的余数的次数统计
    moddict3 = {}
    for i in moddict2.values():
        if i in moddict3:
            moddict3[i] += 1
        else:
            moddict3[i] = 1
    #print(moddict3)

    #moddict3中的模m的余数的次数统计
    moddict4 = {}
    for i in moddict3.values():
        if i in moddict4:
            moddict4[i] += 1
        else:
            moddict4[i] = 1
    #print(moddict4)

    #moddict4中的模m的余数的次数统计
    moddict5 = {}
    for i in moddict4.values():
        if i in moddict5:
            moddict5[i] += 1
        else:
            moddict5[i] = 1
    #print(moddict5)

    #moddict5中的模m的余数的次数统计
    moddict6 = {}
    for i in moddict5.values():
        if i in moddict6:
            moddict6[i] += 1
        else:
            moddict6[i]

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] %= m
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
        s[i + 1] %= m
    from collections import Counter
    c = Counter(s)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[i+1] = b[i] + a[i]
    d = {}
    for i in range(n+1):
        r = b[i] % m
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i]-1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    B = [x % M for x in S]
    from collections import Counter
    C = Counter(B)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 8

def solve(n,m,a):
    sum=0
    for i in range(n):
        sum+=a[i]
    if sum%m==0:
        sum=sum//m
    else:
        sum=sum//m+1
    a.append(0)
    sum=sum%m
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(n):
        dp[i+1]=dp[i]+a[i]
    dp.sort()
    ans=0
    for i in range(n):
        if dp[i+1]-dp[i]>=sum:
            ans+=dp[i+1]-dp[i]-sum
        else:
            ans+=m-(sum-dp[i+1]+dp[i])
    return ans

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    cnt = [0] * m
    for i in range(n + 1):
        cnt[s[i] % m] += 1
    ans = 0
    for i in range(m):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod = [0] * (N + 1)
    for i in range(N):
        mod[i + 1] = (mod[i] + A[i]) % M
    mod_dic = {}
    for i in mod:
        if i in mod_dic:
            mod_dic[i] += 1
        else:
            mod_dic[i] = 1
    ans = 0
    for i in mod_dic:
        ans += mod_dic[i] * (mod_dic[i] - 1) // 2
    print(ans)
