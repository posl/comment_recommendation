Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(i, a, b, c):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + L[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + L[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(ret0, ret1, ret2, ret3)

n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 2

def dfs(i, a, b, c):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10 ** 9
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + L[i], b, c) + 10 if a > 0 else 10 ** 9
    ret2 = dfs(i + 1, a, b + L[i], c) + 10 if b > 0 else 10 ** 9
    ret3 = dfs(i + 1, a, b, c + L[i]) + 10 if c > 0 else 10 ** 9
    return min(ret0, ret1, ret2, ret3)

n, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 3

def dfs(i, a, b, c):
    global ans
    if i == n:
        if min(a, b, c) > 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c)
    dfs(i + 1, a + l[i], b, c)
    dfs(i + 1, a, b + l[i], c)
    dfs(i + 1, a, b, c + l[i])

n, A, B, C = map(int, input().split())
l = [int(input()) for i in range(n)]
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
    dfs(i + 1, a + l[i], b, c)
    dfs(i + 1, a, b + l[i], c)
    dfs(i + 1, a, b, c + l[i])

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = 10 ** 9
dfs(0, 0, 0, 0)
print(ans)

=======
Suggestion 5

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    print(dfs(0, 0, 0, 0))

=======
Suggestion 6

def dfs(i, a, b, c):
    if i == n:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a,b,c) > 0 else float('inf')
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+l[i], b, c) + 10 if a else float('inf')
    ret2 = dfs(i+1, a, b+l[i], c) + 10 if b else float('inf')
    ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c else float('inf')
    ret4 = dfs(i+1, a, b, c) + min(l[i], 10)
    return min(ret0, ret1, ret2, ret3, ret4)

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0,0,0,0))

=======
Suggestion 7

def dfs(now, a, b, c, mp):
    global ans
    if now == N:
        if min(a, b, c) > 0:
            ans = min(ans, mp + abs(a - A) + abs(b - B) + abs(c - C))
        return

    dfs(now + 1, a, b, c, mp)
    dfs(now + 1, a + l[now], b, c, mp + 10 * (a > 0))
    dfs(now + 1, a, b + l[now], c, mp + 10 * (b > 0))
    dfs(now + 1, a, b, c + l[now], mp + 10 * (c > 0))

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
ans = 10 ** 10

dfs(0, 0, 0, 0, 0)
print(ans)

問題文
高橋君��

=======
Suggestion 8

def dfs(depth, a, b, c):
    global ans
    if depth == n:
        if a and b and c:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(depth + 1, a, b, c)
    dfs(depth + 1, a + l[depth], b, c)
    dfs(depth + 1, a, b + l[depth], c)
    dfs(depth + 1, a, b, c + l[depth])

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = float("inf")
dfs(0, 0, 0, 0)
print(ans)

=======
Suggestion 9

def main():
    N,A,B,C = map(int,input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        a,b,c = 0,0,0
        mp = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 1:
                a += l[j]
                mp += 10
            elif (i >> (2*j)) & 3 == 2:
                b += l[j]
                mp += 10
            elif (i >> (2*j)) & 3 == 3:
                c += l[j]
                mp += 10
        if a == 0 or b == 0 or c == 0:
            continue
        mp += abs(A-a) + abs(B-b) + abs(C-c)
        ans = min(ans,mp)
    print(ans)
