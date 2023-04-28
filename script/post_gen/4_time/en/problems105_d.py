Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [0] * m
    for x in s:
        t[x % m] += 1
    ans = 0
    for x in t:
        ans += x * (x - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M

    from collections import Counter
    cnt = Counter(S)

    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2

    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    B = [a % M for a in A]
    from collections import Counter
    C = Counter(B)
    ans = 0
    for k, v in C.items():
        ans += v * (v - 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(n):
        a[i + 1] += a[i]
    r = {}
    for i in a:
        r[i % m] = r.get(i % m, 0) + 1
    ans = 0
    for i in r:
        ans += r[i] * (r[i] - 1) // 2
    print(ans)

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(N):
        A[i + 1] = (A[i] + A[i + 1]) % M
    from collections import Counter
    C = Counter(A)
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)
solve()

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i] = a[i] % m
    s = [0]
    for i in range(n):
        s.append((s[-1] + a[i]) % m)
    from collections import Counter
    c = Counter(s)
    ans = 0
    for k in c:
        ans += c[k] * (c[k] - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 累積和
    acc = [0] * (N+1)
    for i in range(N):
        acc[i+1] = (acc[i] + A[i]) % M

    # 累積和の値をキーとして、同じ値を持つ要素の個数を数える
    from collections import Counter
    c = Counter(acc)
    ans = 0
    for v in c.values():
        ans += v * (v-1) // 2
    print(ans)

=======
Suggestion 8

def readinput():
    nm=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return nm,a

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ans = 0
    if sum % m == 0:
        ans += 1
    for i in range(n):
        ans += a[i:].count(m)
    print(ans)

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]

    from collections import Counter
    c = Counter()
    c[0] = 1
    s = 0
    for a in A:
        s = (s + a) % M
        c[s] += 1

    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2

    print(ans)
