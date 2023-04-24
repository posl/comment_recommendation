Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i, a, b, c):
    if i == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + L[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + L[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 2

def dfs(cur, a, b, c):
    if cur == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + L[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + L[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + L[cur]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 3

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    def dfs(i, a, b, c):
        if i == N:
            return abs(A-a) + abs(B-b) + abs(C-c) - 30 if min(a, b, c) > 0 else float('inf')
        ret0 = dfs(i+1, a, b, c)
        ret1 = dfs(i+1, a+L[i], b, c) + 10
        ret2 = dfs(i+1, a, b+L[i], c) + 10
        ret3 = dfs(i+1, a, b, c+L[i]) + 10
        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, 0, 0))

=======
Suggestion 4

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]

    def dfs(cur, a, b, c):
        if cur == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
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
    dfs(i + 1, a + l[i], b, c) + 10
    dfs(i + 1, a, b + l[i], c) + 10
    dfs(i + 1, a, b, c + l[i]) + 10

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
ans = 10 ** 9

dfs(0, 0, 0, 0)
print(ans)

Thank you for your contribution!

Thank you for your contribution!

Thank you for your contribution!

Thank you for your contribution

=======
Suggestion 6

def solve():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]

    def dfs(cur, a, b, c):
        if cur == N:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')

        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10

        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, 0, 0))

=======
Suggestion 7

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for i in range(N)]

    ans = 10**9

    def dfs(i, a, b, c):
        nonlocal ans
        if i == N:
            if min(a, b, c) > 0:
                ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
            return
        dfs(i + 1, a, b, c)
        dfs(i + 1, a + L[i], b, c) + 10
        dfs(i + 1, a, b + L[i], c) + 10
        dfs(i + 1, a, b, c + L[i]) + 10

    dfs(0, 0, 0, 0)
    print(ans)

=======
Suggestion 8

def solve(N, A, B, C, ls):
    global ans
    if N == 0:
        if C == 0 or B == 0 or A == 0:
            return
        ans = min(ans, abs(A - a) + abs(B - b

=======
Suggestion 9

def main():
    # 入力
    N, A, B, C = map(int, input().split())
    l_list = [int(input()) for _ in range(N)]

    # 処理
    min_mp = 10**10
    for i in range(4**N):
        a = 0
        b = 0
        c = 0
        mp = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 1:
                if a != 0:
                    mp += 10
                a += l_list[j]
            elif (i >> (2*j)) & 3 == 2:
                if b != 0:
                    mp += 10
                b += l_list[j]
            elif (i >> (2*j)) & 3 == 3:
                if c != 0:
                    mp += 10
                c += l_list[j]
        if a != 0 and b != 0 and c != 0:
            mp += abs(a-A) + abs(b-B) + abs(c-C) - 30
            min_mp = min(min_mp, mp)

    # 出力
    print(min_mp)

main()

=======
Suggestion 10

def input():
    return sys.stdin.readline().rstrip()
