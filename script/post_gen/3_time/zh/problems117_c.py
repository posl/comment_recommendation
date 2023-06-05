Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(N, M, X_1, X_2, X_M):
    X_M.sort()
    #print(X_M)
    if N == 1:
        return 0
    elif N == 2:
        return X_M[-1] - X_M[0]
    else:
        min = 100000000000000

=======
Suggestion 2

def solution(N,M,X):
    X.sort()
    if N==1:
        return 0
    else:
        if X[M-1]>0:
            return X[M-1]-X[1]
        else:
            return abs(X[M-2]-X[0])
N,M=map(int,input().split())
X=list(map(int,input().split()))
print(solution(N,M,X))

=======
Suggestion 3

def findMinMoves(N, M, X):
    X.sort()
    if M == 1:
        return 0
    else:
        sum = 0
        for i in range(M - 1):
            sum += X[i + 1] - X[i]
        if N == 1:
            return sum
        else:
            return sum - min(X[1] - X[0], X[M - 1] - X[M - 2])

=======
Suggestion 4

def solution():
    import sys
    import bisect
    N, M = map(int, sys.stdin.readline().strip().split())
    X = list(map(int, sys.stdin.readline().strip().split()))
    X.sort()
    X.append(X[0])
    ans = 0
    for i in range(M):
        if X[i] < 0 < X[i+1]:
            ans += min(-X[i], X[i+1])*2 + max(-X[i], X[i+1])
        else:
            ans += max(X[i], X[i+1]) - min(X[i], X[i+1])
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    else:
        x_diff = []
        for i in range(1, m):
            x_diff.append(x[i] - x[i-1])
        x_diff.sort(reverse=True)
        print(sum(x_diff[n-1:]))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    l = []
    for i in range(m-1):
        l.append(x[i+1] - x[i])
    l.sort()
    print(sum(l[:m-n]))

main()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(x[-1] - x[0])
        return
    x_diff = []
    for i in range(1, m):
        x_diff.append(x[i] - x[i - 1])
    x_diff.sort()
    ans = 0
    for i in range(m - n):
        ans += x_diff[i]
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    X = [int(x) for x in input().split()]
    X.sort()
    if N >= M:
        print(0)
    else:
        Y = []
        for i in range(M-1):
            Y.append(X[i+1]-X[i])
        Y.sort(reverse=True)
        print(sum(Y[N-1:]))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(abs(x[0] - x[-1]))
        return
    x_min = x[0]
    x_max = x[-1]
    x_min_index = 0
    x_max_index = n - 1
    x_min_move = 0
    x_max_move = 0
    for i in range(n):
        if x[i] < 0:
            x_min_move += abs(x[i])
            x_min_index = i
        else:
            x_max_move += abs(x[i])
            x_max_index = i
    if x_min_index == 0 and x_max_index == n - 1:
        print(x_max_move - x_min_move)
    elif x_min_index == 0:
        print(x_max_move - x_min_move + abs(x[x_max_index]))
    elif x_max_index == n - 1:
        print(x_max_move - x_min_move + abs(x[x_min_index]))
    else:
        print(x_max_move - x_min_move + abs(x[x_max_index]) + abs(x[x_min_index]))

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    distance = []
    for i in range(m-1):
        distance.append(x[i+1]-x[i])
    distance.sort()
    print(sum(distance[:m-n]))
