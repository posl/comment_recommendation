Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10 ** 9
    def dfs(cur, a, b, c):
        if cur == N:
            if a == 0 or b == 0 or c == 0:
                return INF
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

=======
Suggestion 2

def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    INF = 10 ** 9
    def dfs(cur, a, b, c):
        if cur == n:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))
    return

=======
Suggestion 3

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10 ** 9
    ans = INF
    for i in range(4 ** N):
        A1 = 0
        B1 = 0
        C1 = 0
        mp = 0
        for j in range(N):
            if (i >> 2 * j) & 3 == 1:
                if A1 != 0:
                    mp += 10
                A1 += l[j]
            elif (i >> 2 * j) & 3 == 2:
                if B1 != 0:
                    mp += 10
                B1 += l[j]
            elif (i >> 2 * j) & 3 == 3:
                if C1 != 0:
                    mp += 10
                C1 += l[j]
        if A1 != 0 and B1 != 0 and C1 != 0:
            mp += abs(A1 - A) + abs(B1 - B) + abs(C1 - C)
            ans = min(ans, mp)
    print(ans)

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline

    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    INF = 10 ** 9
    ans = INF
    for i in range(4 ** N):
        a = []
        b = []
        c = []
        for j in range(N):
            if (i >> (2 * j)) & 3 == 0:
                a.append(L[j])
            elif (i >> (2 * j)) & 3 == 1:
                b.append(L[j])
            elif (i >> (2 * j)) & 3 == 2:
                c.append(L[j])
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue

        mp = 0
        mp += (len(a) - 1) * 10
        mp += (len(b) - 1) * 10
        mp += (len(c) - 1) * 10

        mp += abs(sum(a) - A)
        mp += abs(sum(b) - B)
        mp += abs(sum(c) - C)

        ans = min(ans, mp)

    print(ans)

=======
Suggestion 5

def get_input():
    n,a,b,c = map(int,input().split())
    l = []
    for i in range(n):
        l.append(int(input()))
    return n,a,b,c,l

=======
Suggestion 6

def main():
    n, a, b, c = map(int, input().split())
    ls = [int(input()) for _ in range(n)]
    print(bfs(n, a, b, c, ls))

=======
Suggestion 7

def main():
    # 1行目の入力を取得
    n, a, b, c = map(int, input().split())
    # 2行目以降の入力を取得
    l = [int(input()) for _ in range(

=======
Suggestion 8

def main():
    n,a,b,c=map(int,input().split())
    l=[int(input()) for _ in range(n)]
    ans=10**9
    for i in range(4**n):
        mp=0
        s=[0,0,0,0]
        for j in range(n):
            s[i%(4**(j+1))//(4**j)]+=l[j]
            if i%(4**(j+1))//(4**j)==1:
                mp+=a
            elif i%(4**(j+1))//(4**j)==2:
                mp+=b
            elif i%(4**(j+1))//(4**j)==3:
                mp+=c
        if s[0]==0 or s[1]==0 or s[2]==0:
            continue
        mp+=abs(a-s[0])+abs(b-s[1])+abs(c-s[2])
        ans=min(ans,mp)
    print(ans)

=======
Suggestion 9

def concat(l1, l2):
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    if l1[-1] > l2[-1]:
        return concat(l2, l1)
    else:
        return concat(l1[:-1], l2) + [l1[-1]]

=======
Suggestion 10

def getMinMP(n, a, b, c, l):
    minMP = 10 ** 9
    for i in range(4 ** n):
        tmp = i
        mp = 0
        a1, b1, c1 = 0, 0, 0
        for j in range(n):
            if tmp % 4 == 1:
                a1 += l[j]
                mp += 10
            elif tmp % 4 == 2:
                b1 += l[j]
                mp += 10
            elif tmp % 4 == 3:
                c1 += l[j]
                mp += 10
            tmp //= 4
        if a1 > 0 and b1 > 0 and c1 > 0:
            mp += abs(a - a1) + abs(b - b1) + abs(c - c1)
            minMP = min(mp, minMP)
    return minMP
