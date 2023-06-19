Synthesizing 10/10 solutions

=======
Suggestion 1

def cal_mp(s1,s2,s3):
    return abs(s1-s2)+abs(s2-s3)+abs(s3-s1)

=======
Suggestion 2

def calcMP(target, bambooList):
    if target in bambooList:
        return 0
    if target < min(bambooList):
        return 9999
    if target < 2:
        return 9999
    result = 9999
    for b in bambooList:
        if b < target:
            result = min(result, 1 + calcMP(target - b, bambooList))
    return result

=======
Suggestion 3

def dfs(a,b,c,mp):
    if a==0 and b==0 and c==0:
        return mp
    if a<0 or b<0 or c<0:
        return 1000000
    if (a,b,c) in memo:
        return memo[(a,b,c)]
    ret = 1000000
    for i in range(N):
        ret = min(ret,dfs(a-l[i],b,c,mp+10),dfs(a,b-l[i],c,mp+10),dfs(a,b,c-l[i],mp+10),dfs(a-l[i],b-l[i],c,mp+10),dfs(a-l[i],b,c-l[i],mp+10),dfs(a,b-l[i],c-l[i],mp+10),dfs(a-l[i],b-l[i],c-l[i],mp+10))
    memo[(a,b,c)] = ret
    return ret

N,A,B,C = map(int,input().split())
l = []
for i in range(N):
    l.append(int(input()))
memo = {}
print(dfs(A,B,C,0))

=======
Suggestion 4

def dfs(i, a, b, c, mp):
    if i == n:
        if a != 0 and b != 0 and c != 0:
            return abs(a - A) + abs(b - B) + abs(c - C) + mp - 30
        else:
            return float('inf')
    ret0 = dfs(i + 1, a, b, c, mp)
    ret1 = dfs(i + 1, a + l[i], b, c, mp + 10)
    ret2 = dfs(i + 1, a, b + l[i], c, mp + 10)
    ret3 = dfs(i + 1, a, b, c + l[i], mp + 10)
    return min(ret0, ret1, ret2, ret3)

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0, 0))

=======
Suggestion 5

def dfs(i, a, b, c, mp):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) + mp
    ret = dfs(i + 1, a, b, c, mp)
    ret = min(ret, dfs(i + 1, a + l[i], b, c, mp + (10 if a == 0 else 0)))
    ret = min(ret, dfs(i + 1, a, b + l[i], c, mp + (10 if b == 0 else 0)))
    ret = min(ret, dfs(i + 1, a, b, c + l[i], mp + (10 if c == 0 else 0)))
    return ret

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0, 0))

=======
Suggestion 6

def solve():
    n,a,b,c = map(int,input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10**9
    for i in range(4**n):
        mp = 0
        a1 = a
        b1 = b
        c1 = c
        for j in range(n):
            if i&(1<<j):
                mp += 10
                a1 -= l[j]
            else:
                if j==0:
                    a1 = 0
                mp += 1
        for j in range(n):
            if i&(1<<j):
                if j==0:
                    b1 = 0
                mp += 1
                b1 -= l[j]
            else:
                if j==0:
                    b1 = 0
                mp += 1
        for j in range(n):
            if i&(1<<j):
                if j==0:
                    c1 = 0
                mp += 1
                c1 -= l[j]
            else:
                if j==0:
                    c1 = 0
                mp += 1
        if a1==0 and b1==0 and c1==0:
            ans = min(ans,mp)
    print(ans)
    
solve()

=======
Suggestion 7

def dfs(i, a, b, c):
    if i == n:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else float("inf")
    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + l[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + l[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + l[i]) + 10
    return min(ret0, ret1, ret2, ret3)

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 8

def solve():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10**9
    def dfs(cur, a, b, c):
        if cur == N:
            return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a,b,c)>0 else INF
        ret0 = dfs(cur+1, a, b, c)
        ret1 = dfs(cur+1, a+l[cur], b, c) + 10
        ret2 = dfs(cur+1, a, b+l[cur], c) + 10
        ret3 = dfs(cur+1, a, b, c+l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

solve()

=======
Suggestion 9

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]

    ans = 10 ** 9
    for i in range(4 ** N):
        # 0: 使わない, 1: Aに使う, 2: Bに使う, 3: Cに使う
        tmp = [0, 0, 0, 0]
        mp = 0
        for j in range(N):
            # 0: 使わない, 1: Aに使う, 2: Bに使う, 3: Cに使う
            tmp[3 & (i >> (2 * j))] += l[j]
            if 3 & (i >> (2 * j)) != 0:
                mp += 10
        if tmp[1] != 0 and tmp[2] != 0 and tmp[3] != 0:
            mp += abs(tmp[1] - A) + abs(tmp[2] - B) + abs(tmp[3] - C)
            ans = min(ans, mp)
    print(ans)

=======
Suggestion 10

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10**9
    def dfs(cur, a, b, c):
        if cur == N:
            return abs(A-a) + abs(B-b) + abs(C-c) - 30 if min(a,b,c) > 0 else INF
        ret0 = dfs(cur+1, a, b, c)
        ret1 = dfs(cur+1, a+l[cur], b, c) + 10
        ret2 = dfs(cur+1, a, b+l[cur], c) + 10
        ret3 = dfs(cur+1, a, b, c+l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))
