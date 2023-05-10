Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N, A, B, C = map(int, input().split())
    l = []
    for i in range(N):
        l.append(int(input()))
    print(l)
    print(N, A, B, C)
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])
    print(l[4])
    print(l[5])
    print(l[6])
    print(l[7])
    return

=======
Suggestion 3

def solve():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    INF = 10**9
    def dfs(cur, a, b, c):
        if cur == N:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + L[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + L[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + L[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))
solve()

=======
Suggestion 4

def main():
    n,a,b,c = map(int,input().split())
    l = [int(input()) for i in range(n)]
    ans = 10**9
    for i in range(4**n):
        tmp = [0 for j in range(3)]
        mp = 0
        for j in range(n):
            if i%4 == 0 and tmp[0] > 0:
                mp += 10
            elif i%4 == 1 and tmp[1] > 0:
                mp += 10
            elif i%4 == 2 and tmp[2] > 0:
                mp += 10
            if i%4 == 0:
                tmp[0] += l[j]
            elif i%4 == 1:
                tmp[1] += l[j]
            elif i%4 == 2:
                tmp[2] += l[j]
            i //= 4
        if tmp[0] == 0 or tmp[1] == 0 or tmp[2] == 0:
            continue
        mp += abs(tmp[0]-a) + abs(tmp[1]-b) + abs(tmp[2]-c) - 30
        ans = min(ans,mp)
    print(ans)

=======
Suggestion 5

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    inf = 10 ** 9
    def dfs(cur, a, b, c):
        if cur == n:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return inf
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

=======
Suggestion 6

def main():
    N, A, B, C = map(int, input().split())
    ls = [int(input()) for _ in range(N)]
    INF = 10 ** 9
    def dfs(cur, a, b, c):
        if cur == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + ls[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + ls[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + ls[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

=======
Suggestion 7

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    INF = 10 ** 9
    def dfs(cur, A, B, C):
        if cur == n:
            return abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(A, B, C) > 0 else INF
        ret0 = dfs(cur + 1, A, B, C)
        ret1 = dfs(cur + 1, A + l[cur], B, C) + 10
        ret2 = dfs(cur + 1, A, B + l[cur], C) + 10
        ret3 = dfs(cur + 1, A, B, C + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

=======
Suggestion 8

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10**9
    # DFS
    def dfs(cur, a, b, c):
        if cur == N:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return INF
        # 使わない場合
        ret0 = dfs(cur + 1, a, b, c)
        # Aに使う場合
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        # Bに使う場合
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        # Cに使う場合
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

=======
Suggestion 9

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10 ** 9
    def dfs(cur, a, b, c):
        if cur == N:
            if min(a, b, c) > 0:
                return abs(A - a) + abs(B - b) + abs(C - c) - 30
            else:
                return INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

=======
Suggestion 10

def solve():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 1 << 60
    def dfs(cur, a, b, c):
        if cur == N:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))
solve()
