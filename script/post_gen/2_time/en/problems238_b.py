Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 360
    for i in range(n):
        ans = min(ans, 360 - a[i])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    angles = [0]
    for i in range(n):
        angles.append(angles[-1] + a[i])
    angles = [angle % 360 for angle in angles]
    angles.sort()
    ans = 360
    for i in range(n):
        ans = min(ans, angles[i + 1] - angles[i])
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [360 - a for a in A]
    A = [a if a <= 180 else 360 - a for a in A]
    print(min(A))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    ans = 0
    for a in A:
        ans = 360 - (a + ans) % 360
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = 0
    for i in range(N):
        C += A[i]
    print((360-C)%360)
main()

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A = A[::-1]
    ans = 360
    for i in range(N):
        ans = min(ans, 360 - (ans - A[i]) % 360)
    print(ans)

=======
Suggestion 7

def findMaxAngle(N, A):
    angles = []
    for i in range(N):
        angles.append(sum(A[:i+1])%360)
    angles.sort()
    maxAngle = 0
    for i in range(N):
        maxAngle = max(maxAngle, angles[i-1]-angles[i])
    return 360-maxAngle

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    #print(N, A)

    #a = 0
    #b = 0
    #c = 0
    #d = 0
    #e = 0
    #f = 0
    #g = 0
    #h = 0
    #i = 0
    #j = 0
    #k = 0
    #l = 0
    #m = 0
    #n = 0
    #o = 0
    #p = 0
    #q = 0
    #r = 0
    #s = 0
    #t = 0
    #u = 0
    #v = 0
    #w = 0
    #x = 0
    #y = 0
    #z = 0
    #aa = 0
    #bb = 0
    #cc = 0
    #dd = 0
    #ee = 0
    #ff = 0
    #gg = 0
    #hh = 0
    #ii = 0
    #jj = 0
    #kk = 0
    #ll = 0
    #mm = 0
    #nn = 0
    #oo = 0
    #pp = 0
    #qq = 0
    #rr = 0
    #ss = 0
    #tt = 0
    #uu = 0
    #vv = 0
    #ww = 0
    #xx = 0
    #yy = 0
    #zz = 0
    #aaa = 0
    #bbb = 0
    #ccc = 0
    #ddd = 0
    #eee = 0
    #fff = 0
    #ggg = 0
    #hhh = 0
    #iii = 0
    #jjj = 0
    #kkk = 0
    #lll = 0
    #mmm = 0
    #nnn = 0
    #ooo =

=======
Suggestion 9

def main():
    from sys import stdin
    readline = stdin.readline

    N = int(readline())
    A = list(map(int, readline().split()))

    # 1度でも切ると360度の範囲になるので、
    # 360度で割った余りをとれば、360度に収まる。
    # また、360度を超えた場合は、360度を引けば、360度に収まる。
    # 0度から359度に変換する。
    A = [a % 360 for a in A]
    A = [a if a != 0 else 360 for a in A]

    # 360度の範囲に収まった角度のリストを作成する。
    # 0度から359度のリストを作成する。
    angles = [i for i in range(360)]

    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    # 0度から359度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)

    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    # 0度から359度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)

    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)

    # 360度の範囲に収まった角度のリストの中から、
    # 360度を超えた角度を除外する。
    for a in A:
        angles.remove(a)

    # 360度の範囲に収

=======
Suggestion 10

def main():
    from sys import stdin
    #from math import floor, sqrt, log, log2, log10, sin, cos, tan, pi, inf
    #from collections import deque
    #from itertools import permutations
    #from functools import lru_cache
    #from copy import deepcopy
    #from decimal import Decimal
    #from bisect import bisect_left, bisect_right
    #from heapq import heapify, heappush, heappop
    readline = stdin.readline
    #readlines = stdin.readlines
    #ns = lambda: readline().rstrip()
    #ni = lambda: int(readline().rstrip())
    #nm = lambda: map(int, readline().rstrip().split())
    #nl = lambda: list(map(int, readline().rstrip().split()))
    #nns = lambda: readline().rstrip().split()
    #nns_ = lambda: readline().rstrip().split('_')
    #nni = lambda: int(readline().rstrip().split())
    #nnm = lambda: map(int, readline().rstrip().split())
    #nnl = lambda: list(map(int, readline().rstrip().split()))
    #nnns = lambda: readline().rstrip().split()
    #nnns_ = lambda: readline().rstrip().split('_')
    #nnni = lambda: int(readline().rstrip().split())
    #nnnm = lambda: map(int, readline().rstrip().split())
    #nnnl = lambda: list(map(int, readline().rstrip().split()))
    n = int(input())
    a = list(map(int, input().split()))
    ans = 360
    for i in range(n):
        ans = min(ans, 360 - (a[i] + sum(a[i+1:])))
    print(ans)
