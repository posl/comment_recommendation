Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input_lines():
    while True:
        try:
            line = input()
            yield line
        except EOFError:
            return

=======
Suggestion 2

def get_minimum_change_cost( N, C, D, G ):
    # 2次元配列の初期化
    dp = [ [ 0 for i in range( C ) ] for j in range( N ) ]
    # dp[ i ][ j ] = i列目まで塗り替えて、i列目をj色にしたときの、最小の塗り替えコスト
    # dp[ i ][ j ] = min( dp[ i - 1 ][ k ] ) + D[ k ][ j ] ( k = 0, 1, ..., C - 1 )

    # 初期化
    for i in range( C ):
        dp[ 0 ][ i ] = D[ i ][ G[ 0 ] - 1 ]

    # DP
    for i in range( 1, N ):
        for j in range( C ):
            dp[ i ][ j ] = min( [ dp[ i - 1 ][ k ] for k in range( C ) if k != j ] ) + D[ j ][ G[ i ] - 1 ]

    # 答えは、最後の列の最小値
    return min( dp[ -1 ] )

=======
Suggestion 3

def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]

    rgb = [[0]*c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            rgb[(i+j)%3][c[i][j]-1] += 1

    ans = float('inf')
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(c):
                    tmp += d[l][i]*rgb[0][l]
                    tmp += d[l][j]*rgb[1][l]
                    tmp += d[l][k]*rgb[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def solve():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    # 色の個数を数える
    cnt = [[0]*C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i+j)%3][c[i][j]-1] += 1
    
    # 色の個数の組み合わせを全探索
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                # 各色をどの色に変えるかを決める
                tmp = 0
                for l in range(C):
                    tmp += cnt[0][l] * D[l][i]
                    tmp += cnt[1][l] * D[l][j]
                    tmp += cnt[2][l] * D[l][k]
                ans = min(ans, tmp)
    
    print(ans)

=======
Suggestion 5

def get_ints(): return map(int, input().split())

=======
Suggestion 6

def calc_min_cost(N, C, D, c):
    # dp[i][j] := i 行目まで塗り終わった時の、i 行目の色が j の場合の最小コスト
    dp = [[float('inf')] * C for _ in range(N)]
    for j in range(C):
        dp[0][j] = D[c[0]][j]
    for i in range(1, N):
        for j in range(C):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + D[c[i - 1]][j])
        for j in range(C):
            for k in range(C):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + D[c[i - 1]][j])
    return min(dp[-1])

=======
Suggestion 7

def main():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]

    def calc():
        cnt = [[0] * c for _ in range(3)]
        for i in range(n):
            for j in range(n):
                cnt[(i + j) % 3][c[i][j] - 1] += 1
        cost = [[0] * c for _ in range(3)]
        for i in range(3):
            for j in range(c):
                for k in range(c):
                    cost[i][j] += cnt[i][k] * d[k][j]
        return cost

    cost = calc()
    ans = float('inf')
    for i in range(c):
        for j in range(c):
            if i == j:
                continue
            for k in range(c):
                if i == k or j == k:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

=======
Suggestion 8

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]

    ans = float('inf')
    mod = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            mod[(i + j) % 3][c[i][j] - 1] += 1
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += D[l][i] * mod[0][l]
                    tmp += D[l][j] * mod[1][l]
                    tmp += D[l][k] * mod[2][l]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            cnt[(i + j) % 3][c[i][j] - 1] += 1
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(C):
                    tmp += cnt[0][l] * D[l][i]
                    tmp += cnt[1][l] * D[l][j]
                    tmp += cnt[2][l] * D[l][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 10

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9 + 7
    N,C = map(int,readline().split())
    D = [list(map(int,readline().split())) for _ in range(C)]
    c = [list(map(int,readline().split())) for _ in range(N)]

    ans = 10**18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                tmp = 0
                for l in range(N):
                    for m in range(N):
                        if (l+m)%3 == 0:
                            tmp += D[c[l][m]-1][i]
                        elif (l+m)%3 == 1:
                            tmp += D[c[l][m]-1][j]
                        else:
                            tmp += D[c[l][m]-1][k]
                ans = min(ans,tmp)
    print(ans)
