Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    # 二分探索
    l = 0
    r = 10 ** 10
    while r - l > 10 ** -5:
        mid = (l + r) / 2
        # 人iが明かりjに照らされているか
        is_light = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 <= mid ** 2:
                    is_light[i][j] = 1
        # 人iが少なくとも1つの明かりに照らされているか
        is_lighted = [0] * N
        for i in range(N):
            for j in range(N):
                if is_light[i][j] == 1:
                    is_lighted[i] = 1
        # 人iが少なくとも1つの明かりに照らされている人の数
        lighted_num = 0
        for i in range(N):
            if is_lighted[i] == 1:
                lighted_num += 1
        if lighted_num >= N - K:
            r = mid
        else:
            l = mid
    print(r)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #print(N, K, A, X, Y)

    # 0 から 10^10 までの値を2分探索で求める
    ok = 0
    ng = 10 ** 10
    for _ in range(100):
        mid = (ok + ng) / 2
        #print(ok, ng, mid)
        if is_ok(X, Y, A, mid):
            ng = mid
        else:
            ok = mid
    print(ng)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #print(N, K)
    #print(A)
    #print(X)
    #print(Y)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                #print(i, j, k)
                x1 = X[i]
                y1 = Y[i]
                x2 = X[j]
                y2 = Y[j]
                x3 = X[k]
                y3 = Y[k]
                #print(x1, y1, x2, y2, x3, y3)
                ans = max(ans, solve(x1, y1, x2, y2, x3, y3))
    print(ans)
    return

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    # 人iが人jに照らされているかどうか
    is_illuminated = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            is_illuminated[i][j] = is_illuminated_by(X[i], Y[i], X[j], Y[j])

    # Aに入っている人が照らすことができる人の集合
    can_illuminated = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if is_illuminated[i][j]:
                can_illuminated[i].append(j)

    # Aに入っている人が照らすことができる人の集合の和集合
    can_illuminated_set = set()
    for i in range(K):
        can_illuminated_set = can_illuminated_set | set(can_illuminated[A[i]-1])

    # Aに入っている人が照らすことができる人の集合の和集合から、Aに入っている人を引く
    can_illuminated_set = can_illuminated_set - set(A)

    # Aに入っている人が照らすことができる人の集合の和集合から、Aに入っている人を引いた人の集合
    can_illuminated_set = list(can_illuminated_set)

    # Aに入っている人が照らすことができる人の集合の和集合から、Aに入っている人を引いた人の集合の中で、
    # Aに入っている人が照らすことができる人

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    #print(N,K)
    #print(A)
    #print(X)
    #print(Y)
    #print(X[A[0]-1],Y[A[0]-1])
    #print(X[A[1]-1],Y[A[1]-1])
    #print(X[A[2]-1],Y[A[2]-1])
    #print(X[A[3]-1],Y[A[3]-1])
    #print(X[A[4]-1],Y[A[4]-1])
    #print(X[A[5]-1],Y[A[5]-1])
    #print(X[A[6]-1],Y[A[6]-1])
    #print(X[A[7]-1],Y[A[7]-1])
    #print(X[A[8]-1],Y[A[8]-1])
    #print(X[A[9]-1],Y[A[9]-1])
    #print(X[A[10]-1],Y[A[10]-1])
    #print(X[A[11]-1],Y[A[11]-1])
    #print(X[A[12]-1],Y[A[12]-1])
    #print(X[A[13]-1],Y[A[13]-1])
    #print(X[A[14]-1],Y[A[14]-1])
    #print(X[A[15]-1],Y[A[15]-1])
    #print(X[A[16]-1],Y[A[16]-1])
    #print(X[A[17]-1],Y[A[17]-1])
    #print(X[A[18]-1],Y[A[18]-1])
    #print(X[A[19]-1],Y[A[19]-1])
    #print(X[A[20]-1],Y[A[20]-1])
    #print(X[A[21]-1],Y[A[21]-1])
    #print(X[A[22]-1],Y[A[22]-1])
    #print(X[A[23]-1],Y[A[23]-1])
    #print(X[A[24]-1],Y[A

=======
Suggestion 6

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

=======
Suggestion 7

def main():
    #input
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    Xs = [0] * N
    Ys = [0] * N
    for i in range(N):
        Xs[i], Ys[i] = map(int, input().split())

    #calc
    def dist(x1, y1, x2, y2):
        return (x1-x2)**2 + (y1-y2)**2
    def check(R):
        for i in range(K):
            for j in range(i+1, K):
                if dist(Xs[As[i]-1], Ys[As[i]-1], Xs[As[j]-1], Ys[As[j]-1]) < R**2:
                    return False
        return True

    #output
    l = 0
    r = 10**10
    while r - l > 10**-5:
        m = (l + r) / 2
        if check(m):
            r = m
        else:
            l = m
    print(l)

=======
Suggestion 8

def main():
    import sys
    from math import sqrt
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    # 人iの明かりの強さを求める
    def calc_r(i):
        r = 0
        for j in range(N):
            if i == j:
                continue
            r = max(r, sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) / 2)
        return r

    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]

    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]

    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]

    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]

    # 人iが明かりjによって照らされるかどうか
    def is_in(i, j):
        return sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) <= R[j]

    # 人iが明かりjによって照らされるかどうか

=======
Suggestion 9

def main():
    import sys
    import math
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    # 二分探索
    l = 0
    r = 10**10
    while r - l > 10**(-5):
        m = (l + r) / 2
        # 人iが明かりjに照らされているかの二次元配列
        light = [[False] * K for _ in range(N)]
        for i in range(N):
            for j in range(K):
                if (X[i] - X[A[j] - 1])**2 + (Y[i] - Y[A[j] - 1])**2 <= m**2:
                    light[i][j] = True
        # 人iが照らされている明かりの数
        light_num = [0] * N
        for i in range(N):
            for j in range(K):
                if light[i][j]:
                    light_num[i] += 1
        # 人iが照らされている明かりの数が0の人がいるか
        flag = False
        for i in range(N):
            if light_num[i] == 0:
                flag = True
        if flag:
            l = m
        else:
            r = m
    print(l)

=======
Suggestion 10

def solve():
    import sys
    readline = sys.stdin.readline
    from math import sqrt
    from collections import deque
    from bisect import bisect_left

    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    A = [a-1 for a in A]
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, readline().split())

    def is_ok(R):
        # Rが与えられた時、K人の人がRの明かりを持っている時、
        # すべての人が少なくとも1つの明かりによって照らされるか判定する
        # すべて
