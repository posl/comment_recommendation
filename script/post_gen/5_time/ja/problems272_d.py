Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    print(N, M)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if N == 1:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                print(0)
    elif N == 2:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    print(0, end=' ')
                else:
                    print(1, end=' ')
            print()
    else:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    print(0, end=' ')
                elif i == 1 or j == 1:
                    print(1, end=' ')
                else:
                    print(2, end=' ')
            print()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if (i == 0 and j == 0):
                print(0, end='')
            else:
                print(-1, end='')
            if (j != N-1):
                print(' ', end='')
        print('')

=======
Suggestion 4

def bfs(h,w):
    global n, m
    if n==1:
        if m==1:
            return 0
        else:
            return -1
    if h==0 and w==0:
        return 0
    if h==0:
        if w%2==1:
            return 2
        else:
            return 1
    if w==0:
        if h%2==1:
            return 2
        else:
            return 1
    if h%2==0 and w%2==0:
        return 2
    else:
        return 1

n, m = map(int, input().split())
for i in range(n):
    for j in range(n):
        print(bfs(i,j), end=" ")
    print()

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    if m == 1:
        print(*[0] + [i for i in range(1,n)])
        for i in range(1,n):
            print(*[i+1 for i in range(1,n)])
        exit()
    ans = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = min(i+j,abs(n-i-1)+abs(n-j-1),abs(n-i-1)+j,abs(n-j-1)+i)
    print(*[i for i in ans[0]])
    for i in range(1,n):
        print(*[ans[j][i]+1 for j in range(1,n)])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    M2 = M ** 0.5
    M2 = int(M2)
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            if i - M2 >= 0 and ans[i - M2][j] == -1:
                ans[i - M2][j] = ans[i][j] + 1
            if i + M2 < N and ans[i + M2][j] == -1:
                ans[i + M2][j] = ans[i][j] + 1
            if j - M2 >= 0 and ans[i][j - M2] == -1:
                ans[i][j - M2] = ans[i][j] + 1
            if j + M2 < N and ans[i][j + M2] == -1:
                ans[i][j + M2] = ans[i][j] + 1
    for i in range(N):
        print(*ans[i])

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    if M == 1:
        for i in range(N):
            for j in range(N):
                print(0 if i==j==0 else -1,end=' ')
            print()
        return
    C = [0]*(N*N+1)
    for i in range(N):
        for j in range(N):
            C[(i+1)*(j+1)] = 1
    for k in range(2,N*N+1):
        if C[k] == 1:
            for l in range(2,N*N//k+1):
                C[k*l] = 0
    D = [0]*(N*N+1)
    for i in range(1,N+1):
        for j in range(1,N+1):
            D[i*i+j*j] = 1
    for k in range(2,N*N+1):
        if D[k] == 1:
            for l in range(2,N*N//k+1):
                D[k*l] = 0
    for i in range(N):
        for j in range(N):
            if C[i*N+j+1] == 1 and D[i*i+j*j] == 1:
                print(-1,end=' ')
            else:
                print(i+j,end=' ')
        print()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())

    # N × N のマス目があります。上から i 行目、左から j 列目のマスを (i,j) と表します。
    # 始め、(1,1) に駒が 1 個置かれています。あなたは以下の操作を何度でも行うことができます。
    # 今駒が置かれているマスと距離がちょうど (M)^(1/2) であるマスに駒を移動させる。
    # ここで、マス (i,j) とマス (k,l) の距離は ((i-k)^2+(j-l)^2)^(1/2) とします。
    # 全てのマス (i,j) に対して、以下の問題を解いてください。
    # 駒を (1,1) から (i,j) に移動させることができるかを判定し、できる場合は操作回数の最小値を求めてください。
    #
    # 制約
    # 1 ≦ N ≦ 400
    # 1 ≦ M ≦ 10^6
    # 入力は全て整数
    #
    # 入力
    # 入力は以下の形式で標準入力から与えられる。
    # N M
    #
    # 出力
    # N 行出力せよ。i 行目には N 個の整数を出力せよ。i 行目の j 個目の出力は、マス (i,j) に駒を移動させることができるのであれば操作回数の最小値を、そうでないのであれば -1 を出力せよ。
    #
    # 入力例 1
    # 3 1
    #
