Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    D = []
    for i in range(M - 1):
        D.append(X[i + 1] - X[i])
    D.sort()
    ans = 0
    for i in range(M - N):
        ans += D[i]
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    L = []
    for i in range(1, M):
        L.append(X[i] - X[i - 1])
    L.sort()
    print(sum(L[:M - N]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = [abs(X[i+1]-X[i]) for i in range(M-1)]
    diff.sort(reverse=True)
    print(sum(diff[N-1:]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    L = []
    for i in range(M-1):
        L.append(X[i+1]-X[i])
    #print(L)
    L.sort()
    #print(L)
    if N >= M:
        print(0)
    else:
        print(sum(L[:M-N]))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    #print(N, M, X)
    X.sort()
    #print(X)
    diff = [abs(X[i] - X[i+1]) for i in range(M-1)]
    #print(diff)
    diff.sort(reverse=True)
    #print(diff)
    print(sum(diff[N-1:]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    #X = [-100000, -10, -3, 0, 2, 9, 17]
    #X = [-100000, -10, -3, 0, 2, 9, 17, 100000]
    diff = [X[i+1] - X[i] for i in range(M-1)]
    #print(diff)
    #diff = [90, 7, 3, 2, 7, 8]
    diff.sort()
    #print(diff)
    #diff = [2, 3, 7, 7, 8, 90]
    print(sum(diff[:M-N]))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(N, M)
    #print(X)

    # 前から順に移動する場合の最小移動回数
    #print("前から順に移動する場合の最小移動回数")
    move = 0
    for i in range(M-1):
        move += X[i+1] - X[i]
    #print(move)

    # 後ろから順に移動する場合の最小移動回数
    #print("後ろから順に移動する場合の最小移動回数")
    move2 = 0
    for i in range(M-1, 0, -1):
        move2 += X[i] - X[i-1]
    #print(move2)

    # コマの数が多い場合は、移動しないコマを移動させる
    if N >= M:
        print(0)
    else:
        print(move - move2)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    #print(X[M-1]-X[0])
    diff = [0]*(M-1)
    for i in range(M-1):
        diff[i] = X[i+1]-X[i]
    diff.sort()
    #print(diff)
    if N >= M:
        print(0)
    else:
        for i in range(M-N):
            #print(diff[i])
            X[M-1] -= diff[i]
        print(X[M-1]-X[0])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    #print(N, M)
    #print(X)

    #座標の差を求める
    #X[i+1] - X[i]を求める
    #print(X[1] - X[0])
    #print(X[2] - X[1])
    #print(X[3] - X[2])
    #print(X[4] - X[3])
    #print(X[5] - X[4])
    #print(X[6] - X[5])
    #print(X[7] - X[6])

    #上記の結果をリストに格納する
    #差分のリスト
    #print(X[1] - X[0])
    #print(X[2] - X[1])
    #print(X[3] - X[2])
    #print(X[4] - X[3])
    #print(X[5] - X[4])
    #print(X[6] - X[5])
    #print(X[7] - X[6])
    #print(X[8] - X[7])
    #print(X[9] - X[8])
    #print(X[10] - X[9])

    #print(X[1] - X[0])
    #print(X[2] - X[1])
    #print(X[3] - X[2])
    #print(X[4] - X[3])
    #print(X[5] - X[4])
    #print(X[6] - X[5])
    #print(X[7] - X[6])
    #print(X[8] - X[7])
    #print(X[9] - X[8])
    #print(X[10] - X[9])
    #print(X[11] - X[10])
    #print(X[12] - X[11])
    #print(X[13] - X[12])
    #print(X[14] - X[13])
    #print(X[15] - X[14])
    #print(X[16] - X[15])

=======
Suggestion 10

def main():
    import sys
    from itertools import groupby
    N, M = map(int, sys.stdin.readline().split())
    X = sorted(map(int, sys.stdin.readline().split()))
    Xs = [list(g) for k, g in groupby(X)]
    print(sum(len(xs) - 1 for xs in Xs) + max(len(xs) - 1 for xs in Xs))
