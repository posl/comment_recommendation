Synthesizing 10/10 solutions

=======

def main():
    N, M = map(int, input().split())
    bridge = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        bridge[a] += 1
        bridge[b] += 1
    print(bridge.count(1))

=======

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    ans = 0
    last = 0
    for a, b in bridges:
        if a > last:
            last = b - 1
            ans += 1
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort(key=lambda x: x[1])
    removed = 0
    last = 0
    for a, b in bridges:
        if last < a:
            removed += 1
            last = b - 1
    print(removed)

=======

def main():
    N, M = map(int, input().split())
    lr = []
    for _ in range(M):
        l, r = map(int, input().split())
        lr.append((l, r))
    lr.sort(key=lambda x: x[1])
    ans = 0
    r = 0
    for l, r in lr:
        if r <= l:
            ans += 1
            r = l
    print(ans)

=======

def main():
    n, m = map(int, input().split())
    count = 0
    for i in range(m):
        a, b = map(int, input().split())
        if b - a == 1:
            count += 1
    print(count)

=======

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]

    bridges.sort(key=lambda x: x[1])

    ans = 0
    end = 0
    for a, b in bridges:
        if end < a:
            ans += 1
            end = b - 1

    print(ans)

=======

def main():
    N, M = map(int, input().split())
    req = [list(map(int, input().split())) for _ in range(M)]
    req.sort(key = lambda x: x[1])
    ans = 0
    i = 0
    while i < M:
        j = i
        while j < M and req[i][1] >= req[j][0]:
            j += 1
        i = j
        ans += 1
    print(ans)

=======

def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges = sorted(bridges, key=lambda x: x[1])  # sort by b_i
    ans = 0
    last = 0
    for a, b in bridges:
        if last < a:
            last = b - 1
            ans += 1
    print(ans)

=======

def  solve ( n ,  m ,  ab ) :

=======

def read_int():
    return int(input())
