Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= M
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = (sum_A[i] + A[i]) % M
    from collections import Counter
    c = Counter(sum_A)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=[0]*(n+1)
    for i in range(n):
        b[i+1]=b[i]+a[i]
    c=[0]*m
    for i in range(n+1):
        c[b[i]%m]+=1
    ans=c[0]
    for i in range(m):
        ans+=c[i]*(c[i]-1)//2
    print(ans)

=======
Suggestion 3

def num_divisible_by_m(A, M):
    N = len(A)
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    #print(sum_A)
    #print(sum_A[1:])
    #print(sum_A[1:] % M)
    remainder = [x % M for x in sum_A[1:]]
    #print(remainder)
    from collections import Counter
    c = Counter(remainder)
    #print(c)
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) // 2
    return ans

=======
Suggestion 4

def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 从左到右累积和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # 计算每个余数的个数
    cnt = [0] * m
    for i in range(n + 1):
        cnt[s[i] % m] += 1
    # 计算答案
    ans = 0
    for i in range(m):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n + 1):
        d[s[i] % m] += 1

    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2

    print(ans)

main()

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    mod = {}
    for i in range(n+1):
        if s[i]%m in mod:
            mod[s[i]%m] += 1
        else:
            mod[s[i]%m] = 1
    ans = 0
    for i in mod:
        ans += mod[i]*(mod[i]-1)//2
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 从左到右累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 余数的出现次数
    cnt = [0] * M
    for i in range(N + 1):
        cnt[S[i] % M] += 1

    # 组合
    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2

    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 从左到右累积和
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]

    # 从左到右累积和的模
    t = [x % M for x in s]

    # 模的出现次数
    from collections import defaultdict
    d = defaultdict(int)
    for x in t:
        d[x] += 1

    # 从d中选出两个，计算排列数
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2

    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [a[0]]
    for i in range(1, n):
        s.append(s[i-1] + a[i])
    r = [x % m for x in s]
    from collections import Counter
    c = Counter(r)
    ans = 0
    for x in c:
        if x == 0:
            ans += c[x]
        ans += c[x] * (c[x] - 1) // 2
    print(ans)

=======
Suggestion 10

def solve(n,m,a):
    c=[0]
    for i in range(n):
        c.append(c[-1]+a[i])
    d={}
    for i in range(n+1):
        c[i]%=m
        if c[i] in d:
            d[c[i]]+=1
        else:
            d[c[i]]=1
    ans=0
    for i in d:
        ans+=d[i]*(d[i]-1)//2
    return ans

n,m=map(int,input().split())
a=list(map(int,input().split()))
print(solve(n,m,a))
