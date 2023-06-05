Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(N, A, B, C, L):
    ans = 10**9
    for i in range(4**N):
        a = i
        mp = 0
        p = [0, 0, 0]
        for j in range(N):
            if a % 4 == 1:
                mp += 10
                p[0] += L[j]
            elif a % 4 == 2:
                mp += 10
                p[1] += L[j]
            elif a % 4 == 3:
                mp += 10
                p[2] += L[j]
            a //= 4
        if p[0] == 0 or p[1] == 0 or p[2] == 0:
            continue
        mp += abs(A - p[0]) + abs(B - p[1]) + abs(C - p[2])
        ans = min(ans, mp)
    return ans

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(solve(N, A, B, C, L))

=======
Suggestion 2

def dfs(a,b,c,mp):
    global ans
    if a==0 and b==0 and c==0:
        ans=min(ans,mp)
        return
    if a<0 or b<0 or c<0:
        return
    if mp==0:
        for i in range(n):
            dfs(a-l[i],b,c,mp+1)
            dfs(a,b-l[i],c,mp+1)
            dfs(a,b,c-l[i],mp+1)
    else:
        dfs(a-l[i],b,c,mp+1)
        dfs(a,b-l[i],c,mp+1)
        dfs(a,b,c-l[i],mp+1)
        dfs(a-l[i],b-l[i],c,mp+1)
        dfs(a-l[i],b,c-l[i],mp+1)
        dfs(a,b-l[i],c-l[i],mp+1)
        dfs(a-l[i],b-l[i],c-l[i],mp+1)

n,a,b,c=map(int,input().split())
l=[int(input()) for _ in range(n)]
ans=10000
dfs(a,b,c,0)
print(ans)

=======
Suggestion 3

def dfs(i, a, b, c):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float('inf')
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + l[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + l[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + l[i]) + 10
    return min(ret0, ret1, ret2, ret3)

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 4

def magic(a, b, c, d, e, f, g):
    if a == 0 and b == 0 and c == 0:
        return 0
    if a < 0 or b < 0 or c < 0:
        return 100000000
    return min(magic(a - d, b, c, d, e, f, g) + 1, magic(a, b - e, c, d, e, f, g) + 1, magic(a, b, c - f, d, e, f, g) + 1, magic(a - d, b - e, c, d, e, f, g) + 10, magic(a - d, b, c - f, d, e, f, g) + 10, magic(a, b - e, c - f, d, e, f, g) + 10, magic(a - d, b - e, c - f, d, e, f, g) + 10)

N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
print(magic(A, B, C, l[0], l[1], l[2], l[3]))

=======
Suggestion 5

def dfs(depth, a, b, c):
    if depth == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10 ** 9
    ret0 = dfs(depth + 1, a, b, c)
    ret1 = dfs(depth + 1, a + l[depth], b, c) + 10
    ret2 = dfs(depth + 1, a, b + l[depth], c) + 10
    ret3 = dfs(depth + 1, a, b, c + l[depth]) + 10
    return min(ret0, ret1, ret2, ret3)

n, A, B, C = map(int, input().split())
l = [int(input()) for i in range(n)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 6

def dfs(a,b,c,mp):
    if a==b==c:
        return mp
    if a==0 or b==0 or c==0:
        return float('inf')
    return min(dfs(a-1,b+1,c+1,mp+1),dfs(a-1,b,c,c+10),dfs(a,b-1,c+1,mp+1),dfs(a,b-1,c,c+10),dfs(a,b,c-1,mp+1),dfs(a,b,c-1,c+10))

n,a,b,c=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
print(dfs(a,b,c,0))

=======
Suggestion 7

def dfs(a, b, c, mp, l, n, i):
    if i == n:
        if a == 0 or b == 0 or c == 0:
            return 10**9
        else:
            return mp - 30
    else:
        mp1 = dfs(a, b, c, mp, l, n, i + 1)
        mp2 = dfs(a - l[i], b, c, mp + 10, l, n, i + 1)
        mp3 = dfs(a, b - l[i], c, mp + 10, l, n, i + 1)
        mp4 = dfs(a, b, c - l[i], mp + 10, l, n, i + 1)
        return min(mp1, mp2, mp3, mp4)

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(a, b, c, 0, l, n, 0))

=======
Suggestion 8

def dfs(a, b, c, mp, l):
    if a == 0 and b == 0 and c == 0:
        return mp
    if a < 0 or b < 0 or c < 0:
        return 10 ** 9
    if l == n:
        return 10 ** 9
    if dp[a][b][c][l] != -1:
        return dp[a][b][c][l]
    dp[a][b][c][l] = min(dfs(a - L[l], b, c, mp + 1, l), dfs(a, b - L[l], c, mp + 1, l), dfs(a, b, c - L[l], mp + 1, l), dfs(a + L[l], b + L[l], c, mp + 10, l + 1), dfs(a, b + L[l], c + L[l], mp + 10, l + 1), dfs(a + L[l], b, c + L[l], mp + 10, l + 1), dfs(a + L[l], b + L[l], c + L[l], mp + 10, l + 1))
    return dp[a][b][c][l]

n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]
dp = [[[[0] * (n + 1) for _ in range(101)] for _ in range(101)] for _ in range(101)]
for i in range(101):
    for j in range(101):
        for k in range(101):
            for l in range(n + 1):
                dp[i][j][k][l] = -1
ans = dfs(a, b, c, 0, 0)
print(ans if ans != 10 ** 9 else -1)

=======
Suggestion 9

def dfs(i,a,b,c):
    if i == n:
        if a == 0 or b == 0 or c == 0:
            return float('inf')
        else:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + l[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + l[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + l[i]) + 10
    return min(ret0, ret1, ret2, ret3)

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))
