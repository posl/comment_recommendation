Synthesizing 10/10 solutions

=======
Suggestion 1

def getMPCost(N, A, B, C, ls):
    # 从大到小排序
    ls.sort(reverse=True)
    # 用于记录当前的最小值
    minCost = 100000
    # 用于

=======
Suggestion 2

def get_min_mp(input_list):
    # input_list = [5, 100, 90, 80, 98, 40, 30, 21, 80]
    # input_list = [8, 100, 90, 80, 100, 100, 90, 90, 90, 80, 80, 80]
    # input_list = [8, 1000, 800, 100, 300, 333, 400, 444, 500, 555, 600, 666]
    N = input_list[0]
    A = input_list[1]
    B = input_list[2]
    C = input_list[3]
    l = input_list[4:]
    l.sort(reverse=True)
    # print l

=======
Suggestion 3

def dfs(i, a, b, c):
    if i == n:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return 1000000000
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

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]

    ans = float('inf')
    for i in range(4 ** N):
        a, b, c = 0, 0, 0
        mp = 0
        for j in range(N):
            if i >> 2 * j & 3 == 0:
                continue
            elif i >> 2 * j & 3 == 1:
                mp += 10
                if a != 0:
                    mp += abs(a - l[j])
                a += l[j]
            elif i >> 2 * j & 3 == 2:
                mp += 10
                if b != 0:
                    mp += abs(b - l[j])
                b += l[j]
            elif i >> 2 * j & 3 == 3:
                mp += 10
                if c != 0:
                    mp += abs(c - l[j])
                c += l[j]
        if min(a, b, c) > 0:
            mp += abs(a - A) + abs(b - B) + abs(c - C)
            ans = min(ans, mp)
    print(ans)

=======
Suggestion 5

def dfs(a,b,c,mp):
    global ans
    if a==0 and b==0 and c==0:
        ans=min(ans,mp)
        return
    if mp>ans:
        return
    if a>0:
        dfs(a-1,b,c,mp+10)
    if b>0:
        dfs(a,b-1,c,mp+10)
    if c>0:
        dfs(a,b,c-1,mp+10)
    if a>0 and b>0:
        dfs(a-1,b-1,c,mp+10)
    if b>0 and c>0:
        dfs(a,b-1,c-1,mp+10)
    if c>0 and a>0:
        dfs(a-1,b,c-1,mp+10)
    if a>0 and b>0 and c>0:
        dfs(a-1,b-1,c-1,mp+10)
    if a>0:
        dfs(a-1,b,c,mp+1)
    if b>0:
        dfs(a,b-1,c,mp+1)
    if c>0:
        dfs(a,b,c-1,mp+1)
    if a>1:
        dfs(a-2,b,c,mp+1)
    if b>1:
        dfs(a,b-2,c,mp+1)
    if c>1:
        dfs(a,b,c-2,mp+1)
    if a>0 and b>0:
        dfs(a-1,b-1,c,mp+1)
    if b>0 and c>0:
        dfs(a,b-1,c-1,mp+1)
    if c>0 and a>0:
        dfs(a-1,b,c-1,mp+1)
    if a>0 and b>1:
        dfs(a-1,b-2,c,mp+1)
    if b>0 and c>1:
        dfs(a,b-1,c-2,mp+1)
    if c>0 and a>1:
        dfs(a-2,b,c-1,mp+1)
    if a>1 and b>0:
        dfs(a-2,b-1,c,mp+1)
    if b>1 and c>0:
        dfs(a,b-2,c-1,mp+1)

=======
Suggestion 6

def solve(n, a, b, c, ls):
    if n == 1:
        return abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[0])
    if n == 2:
        return min(abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[0]))
    if n == 3:
        return min(abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[2]),
                   abs(a - ls[0]) + abs(b - ls[2]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[2]),
                   abs(a - ls[1]) + abs(b - ls[2]) + abs(c - ls[0]),
                   abs(a - ls[2]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[2]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[2]),
                   abs(a - ls[0]) + abs(b - ls[2]) + abs(c - ls[0]),
                   abs(a - ls[2]) + abs(b - ls[0]) + abs(c - ls[0]),
                   abs(a - ls[1]) + abs(b - ls[1]) + abs(c - ls[2]),
                   abs(a - ls[1]) + abs(b - ls[2]) + abs(c - ls[1]),
                   abs(a - ls[2]) + abs(b - ls[1]) + abs(c - ls[1]),
                   abs(a - ls[0

=======
Suggestion 7

def dfs(i, a, b, c, mp):
    global ans
    if i == n:
        if min(a, b, c) > 0:
            ans = min(ans, mp + abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(i + 1, a, b, c, mp)
    dfs(i + 1, a + l[i], b, c, mp + 10)
    dfs(i + 1, a, b + l[i], c, mp + 10)
    dfs(i + 1, a, b, c + l[i], mp + 10)


n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = float("inf")
dfs(0, 0, 0, 0, 0)
print(ans)

=======
Suggestion 8

def getMinMP(N, A, B, C, l):
    minMP = 10000
    for i in range(2**N):
        if i == 0:
            continue
        mp = 0
        a = []
        b = []
        c = []
        for j in range(N):
            if (i >> j) & 1:
                a.append(l[j])
            else:
                b.append(l[j])
        for k in range(len(a)):
            mp += a[k]
        for k in range(len(b)):
            mp += b[k]
        if A in a and B in a and C in a:
            mp -= 30
        if A in b and B in b and C in b:
            mp -= 30
        if A in a and B in b and C in b:
            mp -= 10
        if A in b and B in a and C in b:
            mp -= 10
        if A in b and B in b and C in a:
            mp -= 10
        if A in a and B in a and C in b:
            mp -= 10
        if A in b and B in a and C in a:
            mp -= 10
        if A in a and B in b and C in a:
            mp -= 10
        if A in a and B in a and C in a:
            mp -= 20
        if A in b and B in b and C in b:
            mp -= 20
        if mp < minMP:
            minMP = mp
    return minMP

=======
Suggestion 9

def dfs(a,b,c,mp):
    if a == 0 and b == 0 and c == 0:
        return mp
    if a < 0 or b < 0 or c < 0:
        return 1000000
    res = 1000000
    res = min(res,dfs(a-l[0],b,c,mp+1))
    res = min(res,dfs(a,b-l[0],c,mp+1))
    res = min(res,dfs(a,b,c-l[0],mp+1))
    res = min(res,dfs(a-l[0],b-l[0],c,mp+1))
    res = min(res,dfs(a-l[0],b,c-l[0],mp+1))
    res = min(res,dfs(a,b-l[0],c-l[0],mp+1))
    res = min(res,dfs(a-l[0],b-l[0],c-l[0],mp+1))
    return res

n,a,b,c = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
print(dfs(a,b,c,0))

=======
Suggestion 10

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
