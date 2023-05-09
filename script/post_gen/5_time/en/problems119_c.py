Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i, a, b, c):
    if i == n:
        if a > 0 and b > 0 and c > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return float('inf')
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

def solve():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    INF = 10**9
    def dfs(cur, a, b, c):
        if cur == N:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return INF
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + L[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + L[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + L[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))
solve()

=======
Suggestion 3

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10 ** 9

    for i in range(4 ** N):
        a, b, c = 0, 0, 0
        mp = 0
        for j in range(N):
            if (i >> (2 * j)) % 4 == 1:
                if a != 0:
                    mp += 10
                a += l[j]
            elif (i >> (2 * j)) % 4 == 2:
                if b != 0:
                    mp += 10
                b += l[j]
            elif (i >> (2 * j)) % 4 == 3:
                if c != 0:
                    mp += 10
                c += l[j]
        if a == 0 or b == 0 or c == 0:
            continue
        mp += abs(a - A) + abs(b - B) + abs(c - C)
        ans = min(ans, mp)
    print(ans)

=======
Suggestion 4

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for i in range(N)]
    ans = 10**10
    for i in range(4**N):
        mp = 0
        a = []
        b = []
        c = []
        for j in range(N):
            if (i >> (2*j)) & 1 == 1:
                a.append(l[j])
            elif (i >> (2*j + 1)) & 1 == 1:
                b.append(l[j])
            else:
                c.append(l[j])
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue
        mp += (len(a) - 1 + len(b) - 1 + len(c) - 1) * 10
        mp += abs(sum(a) - A)
        mp += abs(sum(b) - B)
        mp += abs(sum(c) - C)
        ans = min(ans, mp)
    print(ans)

=======
Suggestion 5

def main():
    N, A, B, C = map(int, input().split())
    l = [int(input()) for i in range(N)]

    ans = 10**9

    for i in range(4**N):
        a = []
        b = []
        c = []
        mp = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 0:
                a.append(l[j])
            elif (i >> (2*j)) & 3 == 1:
                b.append(l[j])
            elif (i >> (2*j)) & 3 == 2:
                c.append(l[j])

        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue

        mp += (len(a) + len(b) + len(c) - 3) * 10
        mp += abs(sum(a) - A)
        mp += abs(sum(b) - B)
        mp += abs(sum(c) - C)

        ans = min(ans, mp)

    print(ans)

=======
Suggestion 6

def main():
    #N,A,B,C = map(int, input().split())
    #l = [int(input()) for _ in range(N)]
    N,A,B,C = 8,1000,800,100
    l = [300,333,400,444,500,555,600,666]
    #N,A,B,C = 5,100,90,80
    #l = [98,40,30,21,80]
    #N,A,B,C = 5,100,90,80
    #l = [100,100,90,90,90,80,80,80]
    #N,A,B,C = 3,100,90,80
    #l = [100,100,100]
    #N,A,B,C = 3,100,90,80
    #l = [80,90,100]
    #N,A,B,C = 3,100,90,80
    #l = [100,90,80]
    #N,A,B,C = 3,100,90,80
    #l = [100,90,10]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,10]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,20]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,30]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,40]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,50]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,60]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,70]
    #N,A,B,C = 3,100,90,80
    #l = [100,80,80]
    #N,A,B,C = 3,100,90,80
    #l = [100,90,80]
    #N,A,B,C = 3,100,90,80

=======
Suggestion 7

def main():
    n,a,b,c = map(int,input().split())
    l = [int(input()) for _ in range(n)]
    inf = 10**10
    def dfs(cur,a,b,c):
        if cur == n:
            if min(a,b,c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return inf
        ret0 = dfs(cur + 1, a, b, c)
        ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
        ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
        ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0,a,b,c))

=======
Suggestion 8

def find_min_mp(N, A, B, C, l):
    min_mp = 10000
    for a in range(10000):
        for b in range(10000):
            for c in range(10000):
                if a == 0 and b == 0 and c == 0:
                    continue
                mp = 0
                for i in range(N):
                    if l[i] > a:
                        mp += (l[i] - a) * 1
                    elif l[i] < a:
                        mp += (a - l[i]) * 10
                for i in range(N):
                    if l[i] > b:
                        mp += (l[i] - b) * 1
                    elif l[i] < b:
                        mp += (b - l[i]) * 10
                for i in range(N):
                    if l[i] > c:
                        mp += (l[i] - c) * 1
                    elif l[i] < c:
                        mp += (c - l[i]) * 10
                if a == A and b == B and c == C:
                    min_mp = min(min_mp, mp)
    return min_mp

=======
Suggestion 9

def main():
    import sys
    import numpy as np
    import math
    import itertools
    import copy
    input = sys.stdin.readline
    N, A, B, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    ans = 10**6
    for i in itertools.product(range(4), repeat=N):
        a = []
        b = []
        c = []
        for j in range(N):
            if i[j] == 0:
                a.append(l[j])
            elif i[j] == 1:
                b.append(l[j])
            elif i[j] == 2:
                c.append(l[j])
        if len(a) == 0 or len(b) == 0 or len(c) == 0:
            continue
        else:
            mp = 0
            mp += (len(a)-1)*10
            mp += (len(b)-1)*10
            mp += (len(c)-1)*10
            mp += abs(sum(a)-A)
            mp += abs(sum(b)-B)
            mp += abs(sum(c)-C)
            ans = min(ans, mp)
    print(ans)

=======
Suggestion 10

def getMinMP(numBamboos, lengths, targetLengths):
    minMP = float('inf')
    for i in range(2**numBamboos):
        temp = i
        mp = 0
        lengthsCopy = lengths.copy()
        for j in range(numBamboos):
            if temp%2 == 1:
                mp += 10
                lengthsCopy[j] = 0
            temp = temp//2
        if targetLengths[0] in lengthsCopy and targetLengths[1] in lengthsCopy and targetLengths[2] in lengthsCopy:
            minMP = min(minMP, mp)
    return minMP

numBamboos, targetA, targetB, targetC = map(int, input().split())
lengths = []
for i in range(numBamboos):
    lengths.append(int(input()))

targetLengths = [targetA, targetB, targetC]
print(getMinMP(numBamboos, lengths, targetLengths))
