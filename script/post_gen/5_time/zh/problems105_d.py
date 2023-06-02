Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] %= m

    s = [0]
    for i in range(n):
        s.append((s[-1] + a[i]) % m)

    from collections import Counter
    c = Counter(s)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2

    print(ans)

main()

=======
Suggestion 2

def problems105_d():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N):
        if i==0:
            B[i] = A[i]%M
        else:
            B[i] = (B[i-1]+A[i])%M
    B.sort()
    B.append(0)
    ans = 0
    cnt = 1
    for i in range(N):
        if B[i]==B[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt-1)//2
            cnt = 1
    print(ans)

problems105_d()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    mod = [0] * M
    for i in range(N + 1):
        mod[sum_A[i] % M] += 1
    ans = 0
    for i in range(M):
        ans += mod[i] * (mod[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    from collections import Counter
    c = Counter([x%m for x in s])
    ans = 0
    for k,v in c.items():
        ans += v*(v-1)//2
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    cnt = {}
    for x in s:
        if x % m in cnt:
            cnt[x % m] += 1
        else:
            cnt[x % m] = 1
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]*N
    S[0] = A[0]
    for i in range(1,N):
        S[i] = S[i-1]+A[i]
    for i in range(N):
        S[i] = S[i]%M
    from collections import Counter
    cnt = Counter(S)
    ans = 0
    for v in cnt.values():
        ans += v*(v-1)//2
    ans += cnt[0]
    print(ans)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
        S[i + 1] %= M
    from collections import Counter
    C = Counter(S)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = (s[i] + a[i]) % m

    from collections import defaultdict
    d = defaultdict(int)
    for i in s:
        d[i] += 1

    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 从左到右的累积和
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    # 从左到右的累积和除以m的余数
    t = [0] * n
    for i in range(n):
        t[i] = s[i + 1] % m

    from collections import Counter
    c = Counter(t)

    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2

    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    cnt = [0] * M
    for i in range(N + 1):
        cnt[S[i] % M] += 1

    ans = 0
    for i in range(M):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
