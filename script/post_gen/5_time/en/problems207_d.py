Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        s.append(list(map(int,input().split())))
    for _ in range(n):
        t.append(list(map(int,input().split())))
    s.sort()
    t.sort()
    sx = s[0][0]
    sy = s[0][1]
    tx = t[0][0]
    ty = t[0][1]
    for i in range(n):
        s[i][0] -= sx
        s[i][1] -= sy
        t[i][0] -= tx
        t[i][1] -= ty
    s.sort()
    t.sort()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solve():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    s.sort()
    t.sort()
    s = list(map(list, zip(*s)))
    t = list(map(list, zip(*t)))
    if s[0] == t[0]:
        for i in range(n):
            for j in range(n):
                if s[0][i] + s[1][j] == t[0][0] + t[1][0] and s[1][i] + s[0][j] == t[1][0] + t[0][0]:
                    print("Yes")
                    return
        print("No")
    else:
        print("No")
    return

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for _ in range(n):
        a,b = map(int, input().split())
        s.append((a,b))
    t = []
    for _ in range(n):
        a,b = map(int, input().split())
        t.append((a,b))
    if s == t:
        print('Yes')
        return
    for i in range(n):
        s = [(s[i][0]-s[0][0], s[i][1]-s[0][1]) for i in range(n)]
        t = [(t[i][0]-t[0][0], t[i][1]-t[0][1]) for i in range(n)]
        if s == t:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def rotate(x, y, deg):
    rad = deg * math.pi / 180
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)

=======
Suggestion 5

def check(s, t):
    for i in range(len(s)):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            return False
    return True

=======
Suggestion 6

def check(s,t):
    for i in range(len(s)):
        if(s[i][0]!=t[i][0] or s[i][1]!=t[i][1]):
            return False
    return True

=======
Suggestion 7

def check(s, t):
    for i in range(len(s)):
        for j in range(len(s)):
            if (s[i][0] - s[j][0]) * (t[i][1] - t[j][1]) == (s[i][1] - s[j][1]) * (t[i][0] - t[j][0]):
                return True
    return False

n = int(input())
s = []
t = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))
for i in range(n):
    a, b = map(int, input().split())
    t.append((a, b))

=======
Suggestion 8

def check(a,b,c,d):
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    if a == c and b == d:
        return True
    else:
        return False

=======
Suggestion 9

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    import math
    import itertools
    import heapq
    from collections import deque
    from collections import defaultdict
    from collections import Counter

    N = int(readline())
    S = [list(map(int, readline().split())) for _ in range(N)]
    T = [list(map(int, readline().split())) for _ in range(N)]

    def rotate(s, p):
        x, y = s
        rad = math.radians(p)
        return [x*math.cos(rad) - y*math.sin(rad), x*math.sin(rad) + y*math.cos(rad)]

    for i in range(N):
        for j in range(N):
            if S[i] == T[j]:
                for p in range(360):
                    for q in range(-100, 101):
                        for r in range(-100, 101):
                            tmp = [rotate(s, p) for s in S]
                            tmp = [[s[0]+q, s[1]+r] for s in tmp]
                            if tmp == T:
                                print("Yes")
                                exit()
    print("No")

=======
Suggestion 10

def rotate(x, y, p):
    # rotate (x, y) by p degrees
    p = p * math.pi / 180
    return x * math.cos(p) - y * math.sin(p), x * math.sin(p) + y * math.cos(p)
