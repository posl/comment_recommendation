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
    p = 0
    q = 0
    while p < N:
        if L[p] <= R[q]:
            p += 1
            ans += 1
        else:
            q += 1
            ans -= 1
    print(ans)

main()

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())

    L.sort()
    R.sort()

    ans = 0
    i = 0
    j = 0
    cnt = 0
    while i < N and j < N:
        if L[i] <= R[j]:
            cnt += 1
            i += 1
        else:
            cnt -= 1
            j += 1
        ans = max(ans, cnt)

    print(ans)

=======
Suggestion 3

def main():
    n, d = map(int, input().split())
    l = []
    r = []
    for i in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    l.sort()
    r.sort()
    ans = 0
    i = 0
    j = 0
    count = 0
    while i < n:
        if l[i] <= r[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        ans = max(ans, count)
    print(ans)

=======
Suggestion 4

def solve():
    N, D = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if ans >= LR[i][1]:
            continue
        ans = LR[i][0] + D - 1
    print(ans)

=======
Suggestion 5

def main():
    n, d = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(n)]
    walls.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while i < n:
        ans += 1
        j = i + 1
        while j < n and walls[j][0] < walls[i][1]:
            j += 1
        i = j
    print(ans)

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    l_r = []
    for _ in range(n):
        l, r = map(int, input().split())
        l_r.append([l, r])

    l_r.sort(key=lambda x: x[0])

    l = 0
    r = 0
    cnt = 0
    for i in range(n):
        if l_r[i][0] > r:
            l = l_r[i][0]
            r = l_r[i][0] + d - 1
            cnt += 1
        else:
            l = l_r[i][0]
            r = min(l_r[i][1], l_r[i][0] + d - 1)

    print(cnt)

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(N)]
    walls.sort(key=lambda x: x[1])

    ans = 0
    for i in range(N):
        if walls[i][0] - 1 > ans:
            ans += (walls[i][0] - 1 - ans) // D + 1
        ans += (walls[i][1] - walls[i][0] + 1) // D
    print(ans)

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        walls.append(list(map(int, input().split())))
    walls.sort(key=lambda x: x[0])
    # print(walls)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
            continue
        if walls[i][0] - walls[i-1][0] < D:
            if walls[i][1] - walls[i-1][1] < D:
                ans += 1
            else:
                ans += 1
        else:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n,d = map(int,input().split())
    lrs = [list(map(int,input().split())) for _ in range(n)]
    lrs.sort()
    lrs.append([d,d])
    ans = 0
    now = 0
    for i in range(n):
        l,r = lrs[i]
        if l <= now:
            now = max(now,r)
        else:
            ans += (now-l)//d+1
            now = r
    print(ans)

=======
Suggestion 10

def solve(n, d, walls):
    walls.sort()
    walls.append([10**9, 10**9])
    ans = 0
    cur = 0
    for i in range(n):
        while walls[cur][1] < walls[i][0]:
            cur += 1
        ans = max(ans, (walls[cur][0] - walls[i][0] + d - 1) // d + 1)
    return ans
