Synthesizing 10/10 solutions

=======
Suggestion 1

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
        if a[i] == a[i+1]:
            ans += 1
        if b[i] == b[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    AB.sort(key=lambda x: x[1])

    ans = 1
    b = AB[0][1]
    for i in range(1, M):
        if AB[i][0] >= b:
            ans += 1
            b = AB[i][1]

    print(ans)

=======
Suggestion 3

def solve():
    # 入力
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]

    # 各島について、西から何番目の島かを求める
    # 各島について、西から何番目の島かを求める
    west_island = [0] * (N + 1)
    for i, (a, b) in enumerate(AB):
        west_island[a] = i + 1
        west_island[b] = i + 1

    # 西から何番目の島かを求める
    west_island = [0] * (N + 1)
    for i, (a, b) in enumerate(AB):
        west_island[a] = i + 1
        west_island[b] = i + 1

    # 区間を求める
    # 区間を求める
    intervals = []
    start = -1
    for i, island in enumerate(west_island):
        if island == 0:
            continue
        if start == -1:
            start = i
            continue
        if west_island[i - 1] != island:
            intervals.append((start, i - 1))
            start = i
    if start != -1:
        intervals.append((start, N))

    # 区間の個数を求める
    # 区間の個数を求める
    ans = 0
    for i in intervals:
        ans += 1
    print(ans - 1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    AB.sort(key=lambda x: x[1])

    ans = 0
    now = 0

    for a, b in AB:
        if a > now:
            ans += 1
            now = b - 1

    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        a, b = map(int, input().split())
        ab.append([a, b])
    ab.sort()

    ans = 0
    for i in range(m):
        if ab[i][1] in ab[i + 1:]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    AB.sort(key=lambda x: x[1])
    ans = 0
    bridge = [0] * (N + 1)
    for a, b in AB:
        if bridge[a] == 0:
            bridge[b] = 1
        else:
            ans += 1

    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for i in range(M):
        if bridge < AB[i][0]:
            bridge = AB[i][1] - 1
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    AB.sort(key=lambda x:x[1])

    ans = 0
    bridge = [0]*(N+1)
    for i in range(M):
        if bridge[AB[i][0]] == 0:
            bridge[AB[i][1]] = 1
            ans += 1

    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.sort(key=lambda x: x[1])
    ans = 1
    bridge = ab[0][1]
    for i in range(m):
        if ab[i][0] > bridge:
            ans += 1
            bridge = ab[i][1]
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = sorted(a)
    b = sorted(b)
    ans = 0
    for i in range(m):
        if a[i] != a[i-1] and b[i] != b[i-1]:
            ans += 1
    print(ans)
main()
