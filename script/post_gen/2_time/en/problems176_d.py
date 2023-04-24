Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    q = deque([(C_h, C_w, 0)])
    dist = [[float('inf')] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    while q:
        h, w, d = q.popleft()
        if h == D_h and w == D_w:
            print(d)
            return
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                if dist[nh][nw] > d:
                    dist[nh][nw] = d
                    q.appendleft((nh, nw, d))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                    if dist[nh][nw] > d + 1:
                        dist[nh][nw] = d + 1
                        q.append((nh, nw, d + 1))
    print(-1)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    q = deque()
    q.append((C_h, C_w, 0))
    visited = set()
    visited.add((C_h, C_w))
    while q:
        h, w, cnt = q.popleft()
        if h == D_h and w == D_w:
            print(cnt)
            return
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and (nh, nw) not in visited:
                visited.add((nh, nw))
                q.append((nh, nw, cnt))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and (nh, nw) not in visited:
                    visited.add((nh, nw))
                    q.append((nh, nw, cnt + 1))
    print(-1)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    q = deque()
    q.append((C_h, C_w, 0))
    visited = [[False] * W for _ in range(H)]
    visited[C_h][C_w] = True
    while q:
        i, j, cost = q.popleft()
        if i == D_h and j == D_w:
            print(cost)
            return
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            if visited[ni][nj]:
                continue
            if S[ni][nj] == '#':
                continue
            q.append((ni, nj, cost))
            visited[ni][nj] = True
        for di in range(-2, 3):
            for dj in range(-2, 3):
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue
                if visited[ni][nj]:
                    continue
                if S[ni][nj] == '#':
                    continue
                q.append((ni, nj, cost + 1))
                visited[ni][nj] = True
    print(-1)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    dist = [[float('inf')] * w for _ in range(h)]
    dist[ch][cw] = 0
    que = [(ch, cw)]
    while que:
        nh, nw = que.pop(0)
        if nh == dh and nw == dw:
            break
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh += dh
            nw += dw
            if nh < 0 or nh >= h or nw < 0 or nw >= w or s[nh][nw] == '#' or dist[nh][nw] != float('inf'):
                nh -= dh
                nw -= dw
                continue
            dist[nh][nw] = dist[nh-dh][nw-dw] + 1
            que.append((nh, nw))
            nh -= dh
            nw -= dw
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = dh + nh
                nw = dw + nw
                if nh < 0 or nh >= h or nw < 0 or nw >= w or s[nh][nw] == '#' or dist[nh][nw] != float('inf'):
                    nh -= dh
                    nw -= dw
                    continue
                dist[nh][nw] = dist[nh-dh][nw-dw] + 1
                que.append((nh, nw))
                nh -= dh
                nw -= dw
    if dist[dh][dw] == float('inf'):
        print(-1)
    else:
        print(dist[dh][dw])

main()

I got AC, but I think it's not the best solution.

I think the best solution is to use BFS, but I don't know how to implement it.

I think BFS is better than Dijkstra algorithm, because it's unnecessary to calculate the distance between each vertex.

I'm wondering how to implement BFS.

Thank you for reading my question.

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = []
    for h in range(H):
        S.append(list(input()))
    dist = [[-1] * W for _ in range(H)]
    dist[Ch - 1][Cw - 1] = 0
    q = [(Ch - 1, Cw - 1)]
    while q:
        h, w = q.pop(0)
        for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                q.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    q.append((nh, nw))
    print(dist[Dh - 1][Dw - 1])

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[-1]*W for _ in range(H)]
    dist[C_h][C_w] = 0
    Q = [(C_h,C_w)]
    while Q:
        h,w = Q.pop(0)
        for dh,dw in [(0,1),(0,-1),(1,0),(-1,0)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                Q.append((nh,nw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    Q.append((nh,nw))
    print(dist[D_h][D_w])

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = [list(input().rstrip()) for _ in range(H)]
    #print(H, W, Ch, Cw, Dh, Dw, S)
    #for i in range(H):
    #    print(S[i])

    #print("start")
    #print("H", H)
    #print("W", W)
    #print("Ch", Ch)
    #print("Cw", Cw)
    #print("Dh", Dh)
    #print("Dw", Dw)
    #print("S", S)
    #print("S[0]", S[0])
    #print("S[1]", S[1])
    #print("S[2]", S[2])
    #print("S[3]", S[3])

    #print("start")
    #print("H", H)
    #print("W", W)
    #print("Ch", Ch)
    #print("Cw", Cw)
    #print("Dh", Dh)
    #print("Dw", Dw)
    #print("S", S)
    #print("S[0]", S[0])
    #print("S[1]", S[1])
    #print("S[2]", S[2])
    #print("S[3]", S[3])

    #print("start")
    #print("H", H)
    #print("W", W)
    #print("Ch", Ch)
    #print("Cw", Cw)
    #print("Dh", Dh)
    #print("Dw", Dw)
    #print("S", S)
    #print("S[0]", S[0])
    #print("S[1]", S[1])
    #print("S[2]", S[2])
    #print("S[3]", S[3])

    #print("start")
    #print("H", H)
    #print("W", W)
    #print("Ch", Ch)
    #print("Cw", Cw)
    #print("Dh", Dh)
    #print("Dw", Dw)
    #

=======
Suggestion 8

def main():
    #input
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]

    #process
    import collections
    from heapq import heappop, heappush
    INF = 10**9
    dist = [[INF]*W for _ in range(H)]
    dist[C_h-1][C_w-1] = 0
    que = [(0, C_h-1, C_w-1)]
    while que:
        d, h, w = heappop(que)
        if dist[h][w] < d:
            continue
        for dh, dw in ((0,1),(0,-1),(1,0),(-1,0)):
            if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=='.' and dist[h+dh][w+dw]>d:
                dist[h+dh][w+dw] = d
                heappush(que, (d, h+dh, w+dw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=='.' and dist[h+dh][w+dw]>d+1:
                    dist[h+dh][w+dw] = d+1
                    heappush(que, (d+1, h+dh, w+dw))

    #output
    if dist[D_h-1][D_w-1]==INF:
        print(-1)
    else:
        print(dist[D_h-1][D_w-1])

=======
Suggestion 9

def main():
    import sys
    from collections import deque
    H,W = map(int,sys.stdin.readline().split())
    C_h,C_w = map(int,sys.stdin.readline().split())
    D_h,D_w = map(int,sys.stdin.readline().split())
    S = [sys.stdin.readline().rstrip() for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    visited[C_h-1][C_w-1] = True
    que = deque()
    que.append((C_h-1,C_w-1,0))
    while que:
        h,w,cnt = que.popleft()
        if h == D_h-1 and w == D_w-1:
            print(cnt)
            return
        for dh,dw in ((0,1),(1,0),(-1,0),(0,-1)):
            nh,nw = h+dh,w+dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and not visited[nh][nw]:
                visited[nh][nw] = True
                que.append((nh,nw,cnt))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh,nw = h+dh,w+dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "." and not visited[nh][nw]:
                    visited[nh][nw] = True
                    que.append((nh,nw,cnt+1))
    print(-1)

=======
Suggestion 10

def main():
    import sys
    import math
    from collections import deque
    from collections import defaultdict
    from collections import Counter
    from itertools import combinations
    from itertools import permutations
    from itertools import product
    from bisect import bisect_left
    from bisect import bisect_right
    from functools import lru_cache
    from heapq import heappush, heappop
    from math import factorial
    from math import gcd
    from math import log2
    from math import inf
    from operator import itemgetter
    from operator import mul
    from operator import xor
    from string import ascii_lowercase
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline
    def read_int(): return int(input())
    def read_int_n(): return list(map(int, input().split()))
    def read_float(): return float(input())
    def read_float_n(): return list(map(float, input().split()))
    def read_str(): return input().rstrip()
    def read_str_n(): return list(map(str, input().split()))
    def error_print(*args): print(*args, file=sys.stderr)
    INF = 10**18
    MOD = 10**9+7
    # MOD = 998244353

    H, W = read_int_n()
    Ch, Cw = read_int_n()
    Dh, Dw = read_int_n()
    S = [read_str() for _ in range(H)]
    dist = [[INF]*W for _ in range(H)]
    dist[Ch-1][Cw-1] = 0
    que = deque([(Ch-1, Cw-1)])
    while que:
        h, w = que.popleft()
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h+dh, w+dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == '#':
                continue
            if dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            que.appendleft((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2,
