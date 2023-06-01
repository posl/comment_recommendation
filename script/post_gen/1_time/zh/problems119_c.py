Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10 ** 9
    for i in range(4 ** n):
        mp = 0
        la, lb, lc = 0, 0, 0
        for j in range(n):
            if (i >> (2 * j)) % 4 == 1:
                mp += 10
                if la > 0:
                    mp += abs(l[j] - la)
                la += l[j]
            elif (i >> (2 * j)) % 4 == 2:
                mp += 10
                if lb > 0:
                    mp += abs(l[j] - lb)
                lb += l[j]
            elif (i >> (2 * j)) % 4 == 3:
                mp += 10
                if lc > 0:
                    mp += abs(l[j] - lc)
                lc += l[j]
        if la > 0 and lb > 0 and lc > 0:
            mp += abs(la - a) + abs(lb - b) + abs(lc - c)
            ans = min(ans, mp)
    print(ans)

=======
Suggestion 3

def dfs(a, b, c, mp, l, n):
    if n == N:
        if a == 0 or b == 0 or c == 0:
            return 10**9
        else:
            return mp + abs(a - A) + abs(b - B) + abs(c - C) - 30
    ret0 = dfs(a, b, c, mp, l, n + 1)
    ret1 = dfs(a + l[n], b, c, mp + 10, l, n + 1)
    ret2 = dfs(a, b + l[n], c, mp + 10, l, n + 1)
    ret3 = dfs(a, b, c + l[n], mp + 10, l, n + 1)
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0, l, 0))

=======
Suggestion 4

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        tmp = i
        mp = 0
        a = A
        b = B
        c = C
        for j in range(N):
            if tmp % 4 == 1:
                mp += 10
                a -= l[j]
            elif tmp % 4 == 2:
                mp += 10
                b -= l[j]
            elif tmp % 4 == 3:
                mp += 10
                c -= l[j]
            tmp //= 4
        if a <= 0 and b <= 0 and c <= 0:
            ans = min(ans, mp)
    print(ans)

=======
Suggestion 5

def getMinMP(n, a, b, c, ls):
    ls.sort(reverse=True)
    dp = [[[float('inf') for i in range(3001)] for j in range(3001)] for k in range(3001)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(3001):
            for k in range(3001):
                for l in range(3001):
                    if j >= ls[i]:
                        dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j-ls[i]][k]+l)
                    if k >= ls[i]:
                        dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k-ls[i]]+l)
                    dp[i+1][min(j+ls[i], 3000)][k] = min(dp[i+1][min(j+ls[i], 3000)][k], dp[i][j][k]+l)
                    dp[i+1][j][min(k+ls[i], 3000)] = min(dp[i+1][j][min(k+ls[i], 3000)], dp[i][j][k]+l)
                    dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
    res = float('inf')
    for i in range(3001):
        for j in range(3001):
            if i >= a and j >= b and i+j <= 3000:
                res = min(res, dp[n][i][j]+abs(i-a)+abs(j-b)+abs(i+j-c))
    return res

=======
Suggestion 6

def solve():
    N, A, B, C = map(int, input().split())
    l = sorted([int(input()) for _ in range(N)], reverse=True)
    INF = float('inf')
    def dfs(i, a, b, c):
        if i == N:
            return abs(A-a) + abs(B-b) + abs(C-c) - 30 if min(a, b, c) > 0 else INF
        ret0 = dfs(i+1, a, b, c)
        ret1 = dfs(i+1, a+l[i], b, c) + 10
        ret2 = dfs(i+1, a, b+l[i], c) + 10
        ret3 = dfs(i+1, a, b, c+l[i]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

solve()

=======
Suggestion 7

def dfs(i, a, b, c, mp):
    if i == n:
        if a > 0 and b > 0 and c > 0:
            return abs(a - a_) + abs(b - b_) + abs(c - c_) + mp - 30
        else:
            return 10 ** 18
    ret0 = dfs(i + 1, a, b, c, mp)
    ret1 = dfs(i + 1, a + l[i], b, c, mp + 10)
    ret2 = dfs(i + 1, a, b + l[i], c, mp + 10)
    ret3 = dfs(i + 1, a, b, c + l[i], mp + 10)
    return min(ret0, ret1, ret2, ret3)


n, a_, b_, c_ = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0, 0))

=======
Suggestion 8

def getMinMP(N,A,B,C,l):
    #print("N,A,B,C,l:",N,A,B,C,l)
    if N==0:
        if A==0 and B==0 and C==0:
            return 0
        else:
            return 1000000
    if A==0 and B==0 and C==0:
        return 0
    if A<0 or B<0 or C<0:
        return 1000000
    if A==0 and B==0 and C==0:
        return 0
    if l[0]==A or l[0]==B or l[0]==C:
        return getMinMP(N-1,A-l[0],B,C,l[1:])
    else:
        return min(getMinMP(N-1,A,B,C,l[1:]),1+getMinMP(N-1,A-l[0],B,C,l[1:]),1+getMinMP(N-1,A,B-l[0],C,l[1:]),1+getMinMP(N-1,A,B,C-l[0],l[1:]))


N,A,B,C=map(int,input().split())
l=[]
for i in range(N):
    l.append(int(input()))

print(getMinMP(N,A,B,C,l))

=======
Suggestion 9

def main():
    pass
