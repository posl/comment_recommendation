Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = []
    for i in range(M-1):
        diff.append(X[i+1] - X[i])
    diff.sort(reverse=True)
    print(sum(diff[N-1:]))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    D = []
    for i in range(M-1):
        D.append(X[i+1] - X[i])
    D.sort()
    print(sum(D[:max(0, M-N)]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    diff = [X[i+1] - X[i] for i in range(M-1)]
    diff.sort()
    print(sum(diff[:max(0, M-N)]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    d = [0] * (M - 1)
    for i in range(M - 1):
        d[i] = X[i + 1] - X[i]
    d.sort()
    ans = 0
    for i in range(M - N):
        ans += d[i]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    if N >= M:
        print(0)
        return
    D = []
    for i in range(M-1):
        D.append(X[i+1] - X[i])
    D.sort(reverse=True)
    print(sum(D[N-1:]))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))
    D = [X[i+1] - X[i] for i in range(M-1)]
    D.sort()
    print(sum(D[:max(0, M-N)]))

=======
Suggestion 7

def main():
    from bisect import bisect_left
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    if N >= M:
        print(0)
        return
    diff = [X[i + 1] - X[i] for i in range(M - 1)]
    diff.sort()
    print(sum(diff[:M - N]))

main()

=======
Suggestion 8

def solve(N,M,X):
    X.sort()
    if N >= M:
        return 0
    else:
        X_diff = [X[i+1] - X[i] for i in range(M-1)]
        X_diff.sort()
        return sum(X_diff[:M-N])

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    N, M = map(int, input().split())
    X = list(map(int, input().split()))

    X.sort()

    # M個の座標にN個のピースを置いて、M個の座標に移動する
    # 1ピースの移動量は1
    # 1ピースを移動させることで、1ピースの移動量が1増える
    # 1ピースを移動させることで、1ピースの移動量が1減る
    # 1ピースを移動させることで、1ピースの移動量が0になる
    # 1ピースを移動させることで、1ピースの移動量が-1になる
    # 1ピースを移動させることで、1ピースの移動量が-2になる
    # 1ピースを移動させることで、1ピースの移動量が-3になる
    # 1ピースを移動させることで、1ピースの移動量が-4になる
    # 1ピースを移動させることで、1ピースの移動量が-5になる
    # 1ピースを移動させることで、1ピースの移動量が-6になる
    # 1ピースを移動させることで、1ピースの移動量が-7になる
    # 1ピースを移動させることで、1ピースの移動量が-8になる
    # 1ピースを移動させることで、1ピースの移動量が-9になる
    # 1ピースを移動させることで、1ピースの移動量が-10になる
    # 1ピースを移動させることで、

=======
Suggestion 10

def  main():
     # Input 
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
     # Sort 
    X.sort()
     # Calculate the distance between all adjacent coordinates 
    D = []
    for i in range(M - 1):
        D.append(X[i + 1] - X[i])
     # If the number of pieces is greater than or equal to the number of coordinates, 
     # the minimum number of moves is 0. 
    if N >= M:
        print(0)
        return
     # Sort in ascending order 
    D.sort()
     # The sum of the distances between the coordinates of the pieces 
    ans = sum(D[0:M - N])
    print(ans)
