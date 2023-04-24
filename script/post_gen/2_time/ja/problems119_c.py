Synthesizing 10/10 solutions (Duplicates hidden)

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

def dfs(i, a, b, c):
    if i == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10 ** 9
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + L[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + L[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 3

def dfs(i, a, b, c):
    global ans
    if i == N:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + L[i], b, c)
    dfs(i + 1, a, b + L[i], c)
    dfs(i + 1, a, b, c + L[i])

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
ans = 10**9
dfs(0, 0, 0, 0)
print(ans)

=======
Suggestion 4

def dfs(i, a, b, c):
    global ans
    if i == n:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + L[i], b, c) + 10
    dfs(i + 1, a, b + L[i], c) + 10
    dfs(i + 1, a, b, c + L[i]) + 10

n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]
ans = 10 ** 9
dfs(0, 0, 0, 0)
print(ans)

=======
Suggestion 5

def dfs(i, a, b, c):
    global ans
    if i == n:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + L[i], b, c)
    dfs(i + 1, a, b + L[i], c)
    dfs(i + 1, a, b, c + L[i])

n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]
ans = 10 ** 9
dfs(0, 0, 0, 0)
print(ans)

=======
Suggestion 6

def dfs(cur, A, B, C):
    if cur == N:
        if min(A, B, C) > 0:
            return abs(A - a) + abs(B - b) + abs(C - c) - 30
        else:
            return float("inf")

    ret0 = dfs(cur + 1, A, B, C)
    ret1 = dfs(cur + 1, A + l[cur], B, C) + 10
    ret2 = dfs(cur + 1, A, B + l[cur], C) + 10
    ret3 = dfs(cur + 1, A, B, C + l[cur]) + 10
    return min(ret0, ret1, ret2, ret3)

N, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 7

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for i in range(n)]

    def dfs(i, a, b, c):
        if i == n:
            return abs(a-a) + abs(b-b) + abs(c-c) - 30 if min(a, b, c) > 0 else 10**9
        ret0 = dfs(i+1, a, b, c)
        ret1 = dfs(i+1, a+l[i], b, c) + 10 if a else 10**9
        ret2 = dfs(i+1, a, b+l[i], c) + 10 if b else 10**9
        ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c else 10**9
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

=======
Suggestion 8

def dfs(n, a, b, c):
    if n == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else float("inf")
    ret0 = dfs(n+1, a, b, c)
    ret1 = dfs(n+1, a+l[n], b, c) + 10
    ret2 = dfs(n+1, a, b+l[n], c) + 10
    ret3 = dfs(n+1, a, b, c+l[n]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 9

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 100000000
    for i in range(4**N):
        a, b, c = 0, 0, 0
        a_mp, b_mp, c_mp = 0, 0, 0
        for j in range(N):
            if (i >> (j*2)) & 3 == 0:
                a += l[j]
                a_mp += 10 * (l[j]-1)
            elif (i >> (j*2)) & 3 == 1:
                b += l[j]
                b_mp += 10 * (l[j]-1)
            elif (i >> (j*2)) & 3 == 2:
                c += l[j]
                c_mp += 10 * (l[j]-1)
        if a != 0 and b != 0 and c != 0:
            a_mp += abs(a-A)
            b_mp += abs(b-B)
            c_mp += abs(c-C)
            ans = min(ans, a_mp+b_mp+c_mp-30)
    print(ans)
