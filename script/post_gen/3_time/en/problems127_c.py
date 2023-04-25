Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    print(max(min(R) - max(L) + 1, 0))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    print(min(R) - max(L) + 1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    print(max(0, min(R) - max(L) + 1))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    print(min(R) - max(L) + 1)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    L, R = [], []
    for _ in range(M):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    print(min(R) - max(L) + 1 if min(R) >= max(L) else 0)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    l = [0] * N
    r = [0] * N
    for _ in range(M):
        L, R = map(int, input().split())
        l[L-1] += 1
        r[R-1] += 1
    cnt = 0
    ans = 0
    for i in range(N):
        cnt += l[i]
        if cnt == M:
            ans += 1
        cnt -= r[i]
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    LR.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for l, r in LR:
        if l > last:
            ans += 1
            last = r
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    gates = [tuple(map(int, input().split())) for _ in range(M)]
    gates.sort(key=lambda x: x[1])
    ans = 0
    end = 0
    for gate in gates:
        if gate[0] > end:
            end = gate[1]
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    l = []
    for i in range(m):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[1])
    ans = 0
    end = 0
    for i in range(m):
        if end < l[i][0]:
            ans += 1
            end = l[i][1]
    print(ans)
