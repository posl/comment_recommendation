Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    mod = [0] * n
    mod[0] = a[0] % m
    for i in range(1, n):
        mod[i] = (mod[i - 1] + a[i]) % m
    mod.sort()
    ans = 0
    cnt = 1
    for i in range(1, n):
        if mod[i] == mod[i - 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # a[i] = (a[0] + a[1] + ... + a[i]) % m
    for i in range(1, n):
        a[i] += a[i - 1]
    a = [a[i] % m for i in range(n)]

    a.sort()
    a.append(-1)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] == a[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    print(ans)

=======
Suggestion 3

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    sumA = [0]*(N+1)
    for i in range(N):
        sumA[i+1] = sumA[i] + A[i]
    modA = [0]*N
    for i in range(N):
        modA[i] = sumA[i+1] % M
    modA.sort()
    modA.append(-1)
    ans = 0
    c = 1
    for i in range(N):
        if modA[i] == modA[i+1]:
            c += 1
        else:
            ans += c*(c-1)//2
            c = 1
    print(ans)

solve()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    A = [a % M for a in A]
    from collections import Counter
    C = Counter(A)
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    d = {}
    for i in range(n+1):
        s[i] %= m
        if s[i] in d:
            d[s[i]] +=1
        else:
            d[s[i]] = 1
    ans = 0
    for i in d:
        ans += d[i]*(d[i]-1)//2
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    d = {}
    for i in range(n + 1):
        r = s[i] % m
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for r in d:
        ans += d[r] * (d[r] - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i]%=m
    s = [0]
    for i in range(n):
        s.append((s[-1]+a[i])%m)
    from collections import Counter
    c = Counter(s)
    ans = 0
    for x in c.values():
        ans += x*(x-1)//2
    print(ans)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Aの累積和のmod M
    # 累積和のmod Mが同じになる区間の個数を求める
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = (s[i] + A[i]) % M

    from collections import defaultdict
    dd = defaultdict(int)
    for v in s:
        dd[v] += 1

    ans = 0
    for v in dd.values():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 9

def solve(n, m, a):
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [x % m for x in s]
    from collections import defaultdict
    d = defaultdict(int)
    for x in t:
        d[x] += 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    return ans

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n+1):
        d[s[i]%m] += 1
    ans = 0
    for x in d.values():
        ans += x*(x-1)//2
    print(ans)
