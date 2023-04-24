Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    for i in range(N):
        T.append(list(map(int, input().split())))
    for i in range(4):
        if S == T:
            print("Yes")
            return
        for j in range(N):
            S[j][0], S[j][1] = S[j][1], -S[j][0]
    for i in range(4):
        if S == T:
            print("Yes")
            return
        for j in range(N):
            S[j][0], S[j][1] = -S[j][1], S[j][0]
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    for i in range(N):
        T.append(list(map(int, input().split())))
    S = sorted(S)
    T = sorted(T)
    for i in range(N):
        S[i][0] -= S[0][0]
        S[i][1] -= S[0][1]
        T[i][0] -= T[0][0]
        T[i][1] -= T[0][1]
    for i in range(360):
        for j in range(N):
            S[j][0], S[j][1] = S[j][0]*cos(i*pi/180)-S[j][1]*sin(i*pi/180), S[j][0]*sin(i*pi/180)+S[j][1]*cos(i*pi/180)
        S = sorted(S)
        for j in range(N):
            S[j][0] = round(S[j][0], 6)
            S[j][1] = round(S[j][1], 6)
        if S == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(list(map(int, input().split())))
    for i in range(n):
        t.append(list(map(int, input().split())))
    s.sort()
    t.sort()
    for i in range(4):
        if s == t:
            print("Yes")
            exit()
        s = rotate(s, 90)
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int,input().split())))
    for i in range(N):
        T.append(list(map(int,input().split())))

    #S,Tの中心を原点に移動
    S_center = [0,0]
    T_center = [0,0]
    for i in range(N):
        S_center[0] += S[i][0]
        S_center[1] += S[i][1]
        T_center[0] += T[i][0]
        T_center[1] += T[i][1]
    S_center[0] /= N
    S_center[1] /= N
    T_center[0] /= N
    T_center[1] /= N
    for i in range(N):
        S[i][0] -= S_center[0]
        S[i][1] -= S_center[1]
        T[i][0] -= T_center[0]
        T[i][1] -= T_center[1]

    #S,Tの中心を原点に移動した後のSを時計回りに90度回転させる
    for i in range(N):
        S[i][0],S[i][1] = S[i][1],-S[i][0]

    #S,Tの中心を原点に移動した後のSを時計回りに180度回転させる
    for i in range(N):
        S[i][0],S[i][1] = -S[i][0],-S[i][1]

    #S,Tの中心を原点に移動した後のSを時計回りに270度回転させる
    for i in range(N):
        S[i][0],S[i][1] = -S[i][1],S[i][0]

    #S,Tの中心を原点に移動した後のSを時計回りに360度回転させる
    for i in range(N):
        S[i][0],S[i][1] = S[i][0],S[i][1]

    #S,Tの中心を原点に移動した後のSを時

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        S.append([int(i) for i in input().split()])
    for _ in range(N):
        T.append([int(i) for i in input().split()])
    #print(S)
    #print(T)
    
    # まずは回転と移動を行う
    # まずは回転を行う
    # まずは時計回りに270度回転させる
    # 回転行列を用いる
    # 回転行列は
    # | cosθ -sinθ |
    # | sinθ  cosθ |
    # となる
    # 今回は時計回りに270度回転させるので、
    # | cosθ -sinθ |
    # | sinθ  cosθ |
    # となる
    # これをSにかける
    # 今回は時計回りに270度回転させるので、
    # | 0 -1 |
    # | 1  0 |
    # となる
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかける
    # これをSにかける
    # これをTにかける
    # これをTにかける
    # これをSにかけ

=======
Suggestion 6

def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(n)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        for o in range(4):
                            for p in range(4):
                                for q in range(4):
                                    for r in range(4):
                                        for a in range(4):
                                            for b in range(4):
                                                for c in range(4):
                                                    for d in range(4):
                                                        s2 = [[s[j][0],s[j][1]] for j in range(n)]
                                                        t2 = [[t[j][0],t[j][1]] for j in range(n)]
                                                        for j in range(n):
                                                            s2[j][0] += i
                                                            s2[j][1] += j
                                                        for j in range(n):
                                                            s2[j][0] += k
                                                            s2[j][1] += l
                                                        for j in range(n):
                                                            s2[j][0] += m
                                                            s2[j][1] += o
                                                        for j in range(n):
                                                            s2[j][0] += p
                                                            s2[j][1] += q
                                                        for j in range(n):
                                                            s2[j][0] += r
                                                            s2[j][1] += a
                                                        for j in range(n):
                                                            s2[j][0] += b
                                                            s2[j][1] += c
                                                        for j in range(n):
                                                            s2[j][0] += d
                                                        s2.sort()
                                                        t2.sort()
                                                        if s2 == t2:
                                                            print("Yes")
                                                            return
    print("No")

=======
Suggestion 7

def main():
    #入力
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a,b = map(int,input().split())
        S.append((a,b))
    for i in range(N):
        c,d = map(int,input().split())
        T.append((c,d))
    #print(S)
    #print(T)
    #処理
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            dx = S[0][0] - S[i][0]
            dy = S[0][1] - S[i][1]
            #print("dx,dy",dx,dy)
            S_tmp = []
            for k in range(N):
                a = S[k][0] + dx
                b = S[k][1] + dy
                S_tmp.append((a,b))
            #print("S_tmp",S_tmp)
            #print("T",T)
            if S_tmp == T:
                #print("Yes")
                print("Yes")
                return
    print("No")
    return

main()

=======
Suggestion 8

def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    Sx = [s[0] for s in S]
    Sy = [s[1] for s in S]
    Tx = [t[0] for t in T]
    Ty = [t[1] for t in T]
    if N == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
    elif N == 2:
        if S[0][0] == S[1][0]:
            if T[0][0] == T[1][0]:
                if S[0][0] == T[0][0]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        elif S[0][1] == S[1][1]:
            if T[0][1] == T[1][1]:
                if S[0][1] == T[0][1]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            if T[0][0] == T[1][0]:
                print("No")
            elif T[0][1] == T[1][1]:
                print("No")
            else:
                if (S[0][1] - S[1][1]) / (S[0][0] - S[1][0]) == (T[0][1] - T[1][1]) / (T[0][0] - T[1][0]):
                    print("Yes")
                else:
                    print("No")
    elif N == 3:
        if S[0][0] == S[1][0] and S[1][0] == S[2][0]:
            if T[0][0] == T[1][0] and T[1][0] == T[2][0]:
                if S[0][0] == T[0][0]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        elif S[0][1] == S[1][1] and S

=======
Suggestion 9

def main():
    n = int(input())
    s = [tuple(map(int, input().split())) for _ in range(n)]
    t = [tuple(map(int, input().split())) for _ in range(n)]

    # まず、sの重心を原点に移動する
    sx = sum([x for x, y in s]) / n
    sy = sum([y for x, y in s]) / n
    s = [(x - sx, y - sy) for x, y in s]

    # 次に、tの重心を原点に移動する
    tx = sum([x for x, y in t]) / n
    ty = sum([y for x, y in t]) / n
    t = [(x - tx, y - ty) for x, y in t]

    # さらに、sの重心とtの重心が一致するように、tを移動する
    t = [(x + sx - tx, y + sy - ty) for x, y in t]

    # sとtの重心が一致するように、tを移動させる
    # このとき、sとtの重心は原点になる

    # sとtが一致するかを判定する
    s = sorted(s)
    t = sorted(t)
    for i in range(n):
        if s[i] != t[i]:
            print("No")
            return

    print("Yes")

=======
Suggestion 10

def main():
    import sys
    import math
    import itertools
    import collections
    import bisect
    import heapq
    import copy
    import decimal
    import fractions
    import functools
    import operator
    import random
    sys.setrecursionlimit(1000000)
    INF = 10**20
    EPS = 10**-10
    MOD = 10**9 + 7
    PI = math.acos(-1)
    def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
    def I(): return int(sys.stdin.buffer.readline())
    def LS(): return sys.stdin.buffer.readline().rstrip().split()
    def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
    def IR(n): return [I() for _ in range(n)]
    def LIR(n): return [LI() for _ in range(n)]
    def SR(n): return [S() for _ in range(n)]
    def LSR(n): return [LS() for _ in range(n)]
    def SRL(n): return [list(S()) for _ in range(n)]
    def MSRL(n): return [[int(j) for j in list(S())] for _ in range(n)]
    random.seed(0)
    def solve():
        n = I()
        s = LIR(n)
        t = LIR(n)
        for i in range(360):
            p = i * PI / 180
            ss = [(s[i][0] * math.cos(p) - s[i][1] * math.sin(p), s[i][0] * math.sin(p) + s[i][1] * math.cos(p)) for i in range(n)]
            ss.sort()
            t.sort()
            if ss == t:
                print("Yes")
                return
        print("No")
    solve()
