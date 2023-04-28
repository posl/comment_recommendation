Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    ans = 0
    for i in range(N):
        if R[i] - L[i] + 1 >= D:
            ans = N
            break
        if L[i] > R[i-1] + D:
            ans += 1
        elif L[i] <= R[i-1] + D:
            if i == N-1:
                ans += 1
            else:
                if R[i+1] - L[i] + 1 >= D:
                    ans += 1
                else:
                    ans += 2
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        ans += (L[i] - R[i]) * (N - i)
    ans = ans // D
    if ans * D < ans:
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    #print(L)
    #print(R)
    i = 0
    j = 0
    ans = 0
    while i < N:
        while j < N and R[j] < L[i] + D:
            j += 1
        ans += 1
        i = j
    print(ans)

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    l = 0
    r = 0
    ans = 0
    while l < N:
        while r < N and L[r] - L[l] < D:
            r += 1
        l = r
        ans += 1
    print(ans)

main()

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    i = 0
    j = 0
    ans = 0
    while i < N:
        while j < N and R[j] < L[i]:
            j += 1
        ans += 1
        i = i + j + D
    print(ans)

main()

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort(key=lambda x: x[0])
    ans = 0
    while walls:
        ans += 1
        L, R = walls.pop(0)
        while walls and walls[0][0] <= R + D:
            L, R = walls.pop(0)
        R += D
        while walls and walls[0][0] <= R + D:
            L, R = walls.pop(0)
    print(ans)

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    walls = []
    for _ in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort(key = lambda x: x[0])
    ans = 0
    i = 0
    while i < N:
        l = walls[i][0]
        r = walls[i][1]
        while i < N - 1 and walls[i + 1][0] <= r + 1:
            r = max(r, walls[i + 1][1])
            i += 1
        ans += (r - l) // D + 1
        i += 1
    print(ans)

=======
Suggestion 8

def main():
    import sys
    import bisect
    input = sys.stdin.readline
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    L.sort()
    R.sort()
    ans = 0
    for i in range(N):
        x = bisect.bisect_left(R, L[i] + D - 1)
        ans = max(ans, i - x + 1)
    print(ans)

=======
Suggestion 9

def main():
    n, d = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(n)]
    lrs.sort()
    ans = 0
    r = 0
    for i in range(n):
        if r < lrs[i][0]:
            r = lrs[i][0]
        if r + d <= lrs[i][1]:
            ans += 1
            r += d
    print(ans)

main()

=======
Suggestion 10

def get_input():
    return map(int, input().split())
