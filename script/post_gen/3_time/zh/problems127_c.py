Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, m = map(int, input().split())
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        l[a] += 1
        r[b] += 1
    ans = 0
    now = 0
    for i in range(1, n + 1):
        now += l[i]
        if now == m:
            ans += 1
        now -= r[i]
    print(ans)

=======
Suggestion 2

def get_input():
    n,m = input().split()
    n = int(n)
    m = int(m)
    l = []
    r = []
    for i in range(m):
        l_i,r_i = input().split()
        l.append(int(l_i))
        r.append(int(r_i))
    return n,m,l,r

=======
Suggestion 3

def solve():
    n, m = map(int, input().split())
    cards = [0] * (n + 1)
    for i in range(m):
        l, r = map(int, input().split())
        cards[l - 1] += 1
        cards[r] -= 1
    for i in range(1, n + 1):
        cards[i] += cards[i - 1]
    return cards.count(m)

print(solve())

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 5

def check():
    n,m = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        l1,r1 = map(int,input().split())
        l.append(l1)
        r.append(r1)
    l.sort()
    r.sort()
    # print(l)
    # print(r)
    if l[-1] > r[0]:
        return 0
    else:
        return r[0]-l[-1]+1

print(check())

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    if l[m-1] > r[0]:
        print(0)
    else:
        print(r[0] - l[m-1] + 1)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L = max(L)
    R = min(R)
    if R - L + 1 < 0:
        return 0
    else:
        return R - L + 1

=======
Suggestion 8

def solve():
    N,M = map(int,input().split())
    L = []
    R = []
    for i in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    print(max(0,R[0]-L[-1]+1))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    Lmax = max(L)
    Rmin = min(R)
    if Rmin - Lmax + 1 >= 0:
        print(Rmin - Lmax + 1)
    else:
        print(0)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    gate = [0] * (N+2)
    for _ in range(M):
        L, R = map(int, input().split())
        gate[L] += 1
        gate[R+1] -= 1
    for i in range(1, N+1):
        gate[i] += gate[i-1]
    print(gate.count(M))
