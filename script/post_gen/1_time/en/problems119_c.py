Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i, a, b, c):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')

    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + l[i], b, c) + 10
    res2 = dfs(i + 1, a, b + l[i], c) + 10
    res3 = dfs(i + 1, a, b, c + l[i]) + 10
    return min(res0, res1, res2, res3)

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 2

def dfs(i, a, b, c):
    if i == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+l[i], b, c) + 10
    ret2 = dfs(i+1, a, b+l[i], c) + 10
    ret3 = dfs(i+1, a, b, c+l[i]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

import sys
input = sys.stdin.readline

=======
Suggestion 3

def dfs(i, a, b, c):
    if i == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else float('inf')
    res0 = dfs(i+1, a, b, c)
    res1 = dfs(i+1, a+l[i], b, c) + 10
    res2 = dfs(i+1, a, b+l[i], c) + 10
    res3 = dfs(i+1, a, b, c+l[i]) + 10
    return min(res0, res1, res2, res3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 4

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    def dfs(i, a, b, c):
        if i == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10 ** 9

        ret0 = dfs(i + 1, a, b, c)
        ret1 = dfs(i + 1, a + L[i], b, c) + 10
        ret2 = dfs(i + 1, a, b + L[i], c) + 10
        ret3 = dfs(i + 1, a, b, c + L[i]) + 10
        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, 0, 0))

=======
Suggestion 5

def dfs(i, a, b, c):
    global ans
    if i == N:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + L[i], b, c) + 10
    dfs(i + 1, a, b + L[i], c) + 10
    dfs(i + 1, a, b, c + L[i]) + 10

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
ans = float('inf')
dfs(0, 0, 0, 0)
print(ans)

=======
Suggestion 6

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        a, b, c = 0, 0, 0
        cost = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 1:
                a += L[j]
                cost += 10
            elif (i >> (2*j)) & 3 == 2:
                b += L[j]
                cost += 10
            elif (i >> (2*j)) & 3 == 3:
                c += L[j]
                cost += 10
        if a and b and c:
            cost += abs(a-A) + abs(b-B) + abs(c-C) - 30
            ans = min(ans, cost)
    print(ans)

=======
Suggestion 7

def dfs(i, a, b, c):
    if i == N: return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10**9
    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + L[i], b, c) + 10 if a else 10**9
    res2 = dfs(i + 1, a, b + L[i], c) + 10 if b else 10**9
    res3 = dfs(i + 1, a, b, c + L[i]) + 10 if c else 10**9
    return min(res0, res1, res2, res3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 8

def dfs(cur, a, b, c):
    if cur == len(l):
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10**9
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 9

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    INF = 10**9

    def dfs(cur, a, b, c):
        if cur == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + L[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + L[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + L[cur]) + 10
        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, 0, 0))

=======
Suggestion 10

def get_min_mp(n, a, b, c, l):
    if n == 0:
        return 0 if a == b == c == 0 else float('inf')
    ret = float('inf')
    ret = min(ret, get_min_mp(n-1, a, b, c, l) + 10)
    if a > 0:
        ret = min(ret, get_min_mp(n-1, a-l[n-1], b, c, l) + 10)
    if b > 0:
        ret = min(ret, get_min_mp(n-1, a, b-l[n-1], c, l) + 10)
    if c > 0:
        ret = min(ret, get_min_mp(n-1, a, b, c-l[n-1], l) + 10)
    ret = min(ret, get_min_mp(n-1, a, b, c, l) + 1)
    if a > 0:
        ret = min(ret, get_min_mp(n-1, a-min(l[n-1], a), b, c, l) + 1)
    if b > 0:
        ret = min(ret, get_min_mp(n-1, a, b-min(l[n-1], b), c, l) + 1)
    if c > 0:
        ret = min(ret, get_min_mp(n-1, a, b, c-min(l[n-1], c), l) + 1)
    return ret
