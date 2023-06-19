Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(m):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    print(max(0, min(r) - max(l) + 1))

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    L = []
    R = []
    for _ in range(m):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    if L[m-1] > R[0]:
        print(0)
    else:
        print(R[0]-L[m-1]+1)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    L, R = [], []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    if L[-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[-1] + 1)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())

    L.sort()
    R.sort()

    ans = 0
    for i in range(M - 1):
        ans += R[i] - L[i] + 1

    ans += R[M - 1] - L[M - 1] + 1

    print(ans)

=======
Suggestion 5

def main():
    # 输入
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    # 計算
    l_max = max(l)
    r_min = min(r)
    if r_min - l_max >= 0:
        print(r_min - l_max + 1)
    else:
        print(0)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for i in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()

    if L[M-1] > R[0]:
        print(0)
    else:
        print(R[0] - L[M-1] + 1)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    l = 0
    r = n + 1
    for _ in range(m):
        l_i, r_i = map(int, input().split())
        l = max(l, l_i)
        r = min(r, r_i)
    print(max(0, r - l + 1))

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

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
    ans = 0
    for i in range(N):
        if L[-1] <= i + 1 <= R[0]:
            ans += 1
    print(ans)
