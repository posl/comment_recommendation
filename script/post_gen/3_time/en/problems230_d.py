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
    r = 0
    for l in L:
        while r < N and R[r] < l:
            r += 1
        ans = max(ans, r - (l + D - 1) // D)
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
    cnt = 0
    r = 0
    for l in L:
        while r < N and R[r] < l:
            r += 1
        cnt += N - r
    print((cnt + D - 1) // D)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    L = []
    R = []
    for _ in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)

    L.sort()
    R.sort()

    L = [0] + L
    R = [0] + R

    l = 1
    r = 1

    ans = N

    while l <= N and r <= N:
        if L[l] + D - 1 < R[r]:
            l += 1
        else:
            ans = min(ans, N - (l - 1) + (r - 1))
            r += 1

    print(ans)

=======
Suggestion 4

def main():
    N, D = [int(x) for x in input().split()]
    walls = []
    for i in range(N):
        L, R = [int(x) for x in input().split()]
        walls.append([L, R])
    walls.sort()
    #print(walls)
    punches = 0
    i = 0
    while i < N:
        j = i
        while j < N and walls[j][0] <= walls[i][0] + D - 1:
            j += 1
        punches += 1
        i = j
    print(punches)

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append([L, R])
    walls.sort()
    ans = 0
    for i in range(N):
        if walls[i][0] <= D:
            ans += 1
            D = min(D, walls[i][1])
        else:
            break
    print(ans)

=======
Suggestion 6

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append([L, R])
    walls.sort(key=lambda x: x[1])
    #print(walls)
    ans = 0
    i = 0
    while i < N:
        ans += 1
        j = i + 1
        while j < N and walls[j][0] <= walls[i][1] + D:
            j += 1
        i = j
    print(ans)

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    walls = []
    for i in range(n):
        l, r = map(int, input().split())
        walls.append((l, r))
    walls = sorted(walls)

    count = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and walls[j][0] <= walls[i][1] + d:
            j += 1
        count += 1
        i = j
    print(count)

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while i < N:
        ans += 1
        end = walls[i][0] + D - 1
        while i < N and walls[i][0] <= end:
            end = min(end, walls[i][1] + D - 1)
            i += 1
    print(ans)

main()

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    N, D = map(int, input().split())
    wall = []
    for i in range(N):
        L, R = map(int, input().split())
        wall.append([L, R])
    wall.sort()
    # print(wall)
    count = 0
    for i in range(N):
        if wall[i][0] > D:
            count += 1
            D = wall[i][1]
        else:
            D = max(D, wall[i][1])
    print(count + 1)

=======
Suggestion 10

def solve():
    N, D = map(int, input().split())
    LR = []
    for i in range(N):
        LR.append(list(map(int, input().split())))

    LR.sort(key=lambda x: x[0])

    ans = 0
    i = 0
    while i < N:
        ans += 1
        j = i + 1
        while j < N and LR[i][1] >= LR[j][0]:
            j += 1
        i = j
        if i < N:
            i -= 1
            while i < N and LR[i][1] >= LR[i][0] + D:
                i += 1

    print(ans)

solve()
