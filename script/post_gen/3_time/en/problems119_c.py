Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i, a, b, c):
    if i == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + l[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + l[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + l[i]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 2

def dfs(i, a, b, c):
    if i == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10 ** 9
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + L[i], b, c) + 10 if a > 0 else 10 ** 9
    ret2 = dfs(i + 1, a, b + L[i], c) + 10 if b > 0 else 10 ** 9
    ret3 = dfs(i + 1, a, b, c + L[i]) + 10 if c > 0 else 10 ** 9
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 3

def dfs(i, a, b, c):
    if i == N:
        return abs(a - A) + abs(b - B) + abs(c - C) if min(a, b, c) > 0 else float('inf')
    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + L[i], b, c) + 10 if a else float('inf')
    res2 = dfs(i + 1, a, b + L[i], c) + 10 if b else float('inf')
    res3 = dfs(i + 1, a, b, c + L[i]) + 10 if c else float('inf')
    return min(res0, res1, res2, res3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 4

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    print(dfs(0, 0, 0, 0))

=======
Suggestion 5

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for i in range(N)]
    print(dfs(0, 0, 0, 0))

=======
Suggestion 6

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    ans = float('inf')

    def dfs(cur, a, b, c):
        nonlocal ans
        if cur == N:
            if min(a, b, c) > 0:
                ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
            return
        dfs(cur + 1, a, b, c)
        dfs(cur + 1, a + L[cur], b, c) + 10
        dfs(cur + 1, a, b + L[cur], c) + 10
        dfs(cur + 1, a, b, c + L[cur]) + 10

    dfs(0, 0, 0, 0)
    print(ans)

=======
Suggestion 7

def get_input():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for i in range(n)]
    return n, a, b, c, l

=======
Suggestion 8

def search(n, a, b, c, l, mp):
    if n == len(l):
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return 1000000000
    mp1 = search(n + 1, a, b, c, l, mp)
    mp2 = search(n + 1, a + l[n], b, c, l, mp + 10)
    mp3 = search(n + 1, a, b + l[n], c, l, mp + 10)
    mp4 = search(n + 1, a, b, c + l[n], l, mp + 10)
    return min(mp1, mp2, mp3, mp4)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(search(0, 0, 0, 0, L, 0))

8 1000 800 100
300
333
400
444
500
555
600
666

243

=======
Suggestion 9

def solve(N,A,B,C,l):
    if N == 0:
        return 0 if min(A,B,C) > 0 else float('inf')
    ret = float('inf')
    ret = min(ret, solve(N-1,A,B,C,l) + 10)
    ret = min(ret, solve(N-1,A-l[N],B,C,l) + 10)
    ret = min(ret, solve(N-1,A,B-l[N],C,l) + 10)
    ret = min(ret, solve(N-1,A,B,C-l[N],l) + 10)
    return ret

N,A,B,C = map(int,input().split())
l = [int(input()) for _ in range(N)]
print(solve(N,A,B,C,l))

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
