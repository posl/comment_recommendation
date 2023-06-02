Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n,a,b,c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10**9
    for i in range(4**n):
        mp = 0
        abc = [0,0,0]
        for j in range(n):
            if (i>>2*j)&1:
                mp+=10
                continue
            if abc[0]!=0:
                mp+=abs(abc[0]-l[j])
            abc[0]=l[j]
        for j in range(n):
            if (i>>2*j)&1==0:
                mp+=10
                continue
            if abc[1]!=0:
                mp+=abs(abc[1]-l[j])
            abc[1]=l[j]
        for j in range(n):
            if (i>>2*j)&1==0:
                mp+=10
                continue
            if abc[2]!=0:
                mp+=abs(abc[2]-l[j])
            abc[2]=l[j]
        if abc[0]*abc[1]*abc[2]==0:continue
        mp+=abs(abc[0]-a)+abs(abc[1]-b)+abs(abc[2]-c)
        ans=min(ans,mp)
    print(ans)

=======
Suggestion 2

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10**9

    def dfs(cur, mp, a, b, c):
        if cur == n:
            if min(a, b, c) > 0:
                return mp + abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return 10**9
        ret0 = dfs(cur + 1, mp, a, b, c)
        ret1 = dfs(cur + 1, mp + 10, a + l[cur], b, c)
        ret2 = dfs(cur + 1, mp + 10, a, b + l[cur], c)
        ret3 = dfs(cur + 1, mp + 10, a, b, c + l[cur])
        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, a, b, c))

=======
Suggestion 3

def get_magic_number(N, A, B, C, l):
    min_magic = 100000000
    for i in range(4 ** N):
        magic = 0
        a = 0
        b = 0
        c = 0
        for j in range(N):
            if i % 4 == 0:
                a += l[j]
                magic += 10
            elif i % 4 == 1:
                b += l[j]
                magic += 10
            elif i % 4 == 2:
                c += l[j]
                magic += 10
            i = i // 4
        if a > 0 and b > 0 and c > 0:
            magic += abs(a - A) + abs(b - B) + abs(c - C)
            if magic < min_magic:
                min_magic = magic
    return min_magic

=======
Suggestion 4

def solve(n, a, b, c, ls):
    #print(n, a, b, c, ls)
    if n == 1:
        return abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[0])
    elif n == 2:
        return min(abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[0]))
    else:
        return min(solve(n - 1, a, b, c, ls[:n - 1]) + abs(c - ls[n - 1]),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(b - ls[n - 1]),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a - ls[n - 1]),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a + b - ls[n - 1] * 2),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a + c - ls[n - 1] * 2),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(b + c - ls[n - 1] * 2),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a + b + c - ls[n - 1] * 3),
                   solve(n - 1, a, b, c, ls[:n - 1]))

=======
Suggestion 5

def solve():
    N,A,B,C = map(int,input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10**9
    ans = INF
    for i in range(4**N):
        mp = 0
        a,b,c = 0,0,0
        for j in range(N):
            if (i >> (2*j)) & 3 == 0:
                continue
            elif (i >> (2*j)) & 3 == 1:
                mp += 10
                a += l[j]
            elif (i >> (2*j)) & 3 == 2:
                mp += 10
                b += l[j]
            elif (i >> (2*j)) & 3 == 3:
                mp += 10
                c += l[j]
        if min(a,b,c) > 0:
            ans = min(ans,mp+abs(A-a)+abs(B-b)+abs(C-c))
    print(ans)

=======
Suggestion 6

def get_min_mp(N, A, B, C, l_list):
    if A in l_list and B in l_list and C in l_list:
        return 0
    mp = 100000
    for i in range(3**N):
        a = A
        b = B
        c = C
        mp_tmp = 0
        for j in range(N):
            if i % 3 == 0:
                a -= l_list[j]
                mp_tmp += 10
            elif i % 3 == 1:
                b -= l_list[j]
                mp_tmp += 10
            else:
                c -= l_list[j]
                mp_tmp += 10
            i = int(i / 3)
        if a == 0 and b == 0 and c == 0:
            mp = min(mp, mp_tmp)
    return mp

=======
Suggestion 7

def dfs(depth, a, b, c):
    global ans
    if depth == n:
        if a != 0 and b != 0 and c != 0:
            ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) - 30)
        return
    dfs(depth + 1, a, b, c)
    dfs(depth + 1, a + l[depth], b, c)
    dfs(depth + 1, a, b + l[depth], c)
    dfs(depth + 1, a, b, c + l[depth])

n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = 10 ** 9
dfs(0, 0, 0, 0)
print(ans)

=======
Suggestion 8

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10 ** 9
    for i in range(4 ** n):
        tmp = i
        mp = 0
        la = []
        for j in range(n):
            la.append(tmp % 4)
            tmp //= 4
        if 0 in la[:3]:
            continue
        if 0 not in la[3:]:
            continue
        if 0 in la[3:]:
            mp = 10 * (la.count(0) - 3)
        ta = tb = tc = 0
        for j in range(n):
            if la[j] == 1:
                ta += l[j]
            elif la[j] == 2:
                tb += l[j]
            elif la[j] == 3:
                tc += l[j]
        if ta == 0 or tb == 0 or tc == 0:
            continue
        mp += abs(ta - a) + abs(tb - b) + abs(tc - c)
        ans = min(ans, mp)
    print(ans)

=======
Suggestion 9

def main():
    pass
