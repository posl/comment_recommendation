Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m=list(map(int,input().split()))
    ab=[]
    for _ in range(m):
        a,b=list(map(int,input().split()))
        ab.append((a,b))
    return n,m,ab

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    ans = 0
    for i in range(1, N):
        if A[-1] < i or B[0] > i:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    print(min(A[0] - 1, N - A[-1], B[0] - 1, N - B[-1]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    A.sort()
    B.sort()

    ans = 0
    for i in range(1, N):
        ans = max(ans, B[0] - A[-1], B[-1] - A[0])

    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a, b = [0] * m, [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    a.sort()
    b.sort()
    cnt = 0
    i, j = 0, 0
    while i < m and j < m:
        if a[i] <= b[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
    print(cnt)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()

    ans = 0
    for i in range(m):
        if a[i] < b[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    right = 0
    for a, b in AB:
        if right < a:
            right = b - 1
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = []
    for _ in range(M):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for ab in AB:
        if ab[0] > bridge:
            bridge = ab[1] - 1
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    a.sort(key=lambda x: x[1])
    cnt = 0
    bridge = 0
    for i in range(m):
        if a[i][0] > bridge:
            cnt += 1
            bridge = a[i][1] - 1
    print(cnt)

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    requests = [tuple(map(int, input().split())) for _ in range(M)]
    bridge = [0] * (N + 1)
    for a, b in requests:
        bridge[a] += 1
        bridge[b] += 1
    print(bridge.count(1))
