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
        l = L[i]
        r = l + D - 1
        if r > R[i]:
            continue
        else:
            ans += 1
            L[i] = r + 1
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
    ans = N
    i = 0
    j = 0
    while i < N:
        if L[i] - R[j] > D:
            ans -= 1
            j += 1
        else:
            i += 1
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
    L = sorted(L)
    R = sorted(R)
    cnt = 0
    for i in range(N):
        if R[i] - L[i] + 1 < D:
            cnt += 1
        else:
            cnt += 2
    print(cnt)

=======
Suggestion 4

def main():
    N,D = map(int,input().split())
    L = [0]*N
    R = [0]*N
    for i in range(N):
        L[i],R[i] = map(int,input().split())
    #print(N,D)
    #print(L)
    #print(R)
    L.sort()
    R.sort()
    #print(L)
    #print(R)
    ans = 0
    for i in range(N):
        if L[i] + D - 1 < R[i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    wall = []
    for i in range(N):
        L, R = map(int, input().split())
        wall.a

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append([L, R])
    walls.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if walls[j][0] - walls[i][1] > D:
                break
            if walls[j][1] - walls[i][0] <= D:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    N, D = map(int, input().split())
    L = []
    R = []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    R.sort()
    L.sort()
    ans = 0
    for i in range(N):
        if L[i] + D - 1 >= R[i]:
            ans += 1
        else:
            j = bisect.bisect_left(R, L[i] + D)
            ans += N - j
    print(ans)

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[0])
    ans = 0
    while walls:
        ans += 1
        start = walls[0][0]
        for i in range(len(walls)):
            if walls[i][0] - start >= D:
                walls = walls[i:]
                break
            if walls[i][1] - start >= D:
                walls = walls[i+1:]
                break
    print(ans)

=======
Suggestion 9

def main():
    n, d = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[0])
    ans = 0
    r = 0
    for i in range(n):
        if l[i][1] <= r:
            continue
        if l[i][0] > r:
            r = l[i][0]
        ans += (l[i][1] - r) // d + 1
        r += ((l[i][1] - r) // d + 1) * d
    print(ans)

=======
Suggestion 10

def main():
    N, D = map(int, input().split())
    wall = [list(map(int, input().split())) for _ in range(N)]
    wall.sort(key=lambda x:x[0])
    ans = 0
    while len(wall) > 0:
        ans += 1
        wall.sort(key=lambda x:x[0])
        now = wall[0][0]
        del wall[0]
        for i in range(len(wall)):
            if wall[i][0] <= now < wall[i][1]:
                wall[i][0] = now + D
            if wall[i][1] <= now + D:
                del wall[i]
                break
    print(ans)
