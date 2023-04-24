Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    D[i][j] = float("inf")
    for i in range(N):
        for j in range(N):
            c[i][j] -= 1
    dp = [[[0] * C for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            for k in range(C):
                dp[(i + j) % 3][c[i][j]][k] += D[c[i][j]][k]
    ans = float("inf")
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, dp[0][i][j] + dp[1][j][k] + dp[2][k][i])
    print(ans)

=======
Suggestion 2

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    grid = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            grid[(i + j) % 3][c[i][j] - 1] += 1
    ans = 10 ** 9
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i != j and i != k and j != k:
                    tmp = 0
                    for l in range(C):
                        tmp += D[l][i] * grid[0][l]
                        tmp += D[l][j] * grid[1][l]
                        tmp += D[l][k] * grid[2][l]
                    ans = min(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    for i in range(C):
        for j in range(C):
            D[i][j] = min(D[i][j], D[i][0] + D[0][j])
    ans = 10 ** 18
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if i == k or j == k:
                    continue
                res = 0
                for l in range(N):
                    for m in range(N):
                        if (l + m) % 3 == 0:
                            res += D[c[l][m] - 1][i]
                        elif (l + m) % 3 == 1:
                            res += D[c[l][m] - 1][j]
                        else:
                            res += D[c[l][m] - 1][k]
                ans = min(ans, res)
    print(ans)

=======
Suggestion 4

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    
    # 3色に分ける
    C1 = [] # 0, 3, 6, 9, ...
    C2 = [] # 1, 4, 7, 10, ...
    C3 = [] # 2, 5, 8, 11, ...
    for i in range(N):
        for j in range(N):
            if (i + j) % 3 == 0:
                C1.append(c[i][j] - 1)
            elif (i + j) % 3 == 1:
                C2.append(c[i][j] - 1)
            else:
                C3.append(c[i][j] - 1)
    
    # 3色に分けたものをそれぞれ色を変えるコストの最小値を求める
    cost = [[0] * C for _ in range(3)]
    for i in range(C):
        for j in range(C):
            cost[0][i] += D[j][i] * C1.count(j)
            cost[1][i] += D[j][i] * C2.count(j)
            cost[2][i] += D[j][i] * C3.count(j)
    
    # 3色に分けたものをそれぞれ色を変えるコストの最小値の最小値を求める
    ans = 10 ** 10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

=======
Suggestion 5

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 0, 1, 2の色について
    # 0: 1, 2, 3
    # 1: 2, 3, 1
    # 2: 3, 1, 2
    # という順番で塗るときの最小コスト
    min_cost = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            for k in range(3):
                min_cost[k][c[i][j] - 1] += D[k][c[i][j] - 1]
    ans = float('inf')
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                cost = min_cost[0][i] + min_cost[1][j] + min_cost[2][k]
                ans = min(ans, cost)
    print(ans)

=======
Suggestion 6

def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    C = [list(map(int, input().split())) for _ in range(N)]
    for k in range(C):
        for i in range(C):
            for j in range(C):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    A = [[0] * C for _ in range(3)]
    for i in range(N):
        for j in range(N):
            A[(i + j) % 3][C[i][j] - 1] += 1
    ans = 10**10
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                ans = min(ans, D[i][j] * A[0][j] + D[j][k] * A[1][k] + D[k][i] * A[2][i])
    print(ans)

main()

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 1. 3色に分類する
    # 2. 3色のうち1色を選ぶ
    # 3. 3色のうち2色を選ぶ
    # 4. 3色のうち3色を選ぶ
    # 5. 3色のうち2色を選ぶ
    # 6. 3色のうち1色を選ぶ
    # 7. 3色のうち3色を選ぶ
    # 8. 3色のうち2色を選ぶ
    # 9. 3色のうち1色を選ぶ
    # 10. 3色のうち2色を選ぶ
    # 11. 3色のうち3色を選ぶ
    # 12. 3色のうち1色を選ぶ
    # 13. 3色のうち2色を選ぶ
    # 14. 3色のうち3色を選ぶ
    # 15. 3色のうち1色を選ぶ
    # 16. 3色のうち2色を選ぶ
    # 17. 3色のうち3色を選ぶ
    # 18. 3色のうち1色を選ぶ
    # 19. 3色のうち2色を選ぶ
    # 20. 3色のうち3色を選ぶ
    # 21. 3色のうち1色を選ぶ
    # 22. 3色のうち2色を選ぶ
    # 23. 3色のうち3色を選ぶ
    # 24. 3

=======
Suggestion 8

def main():
    n,c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    c = [list(map(int, input().split())) for _ in range(n)]
    cost = [[0]*c for _ in range(3)]
    for i in range(n):
        for j in range(n):
            cost[(i+j)%3][c[i][j]-1] += 1
    ans = float('inf')
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i == j or j == k or k == i:
                    continue
                tmp = 0
                for l in range(c):
                    tmp += cost[0][l]*d[l][i]
                    tmp += cost[1][l]*d[l][j]
                    tmp += cost[2][l]*d[l][k]
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    #input
    N, C = map(int, input().split())
    D = [[int(i) for i in input().split()] for _ in range(C)]
    c = [[int(i) for i in input().split()] for _ in range(N)]

    #solve
    ans = 10**15
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                cost = 0
                for l in range(N):
                    for m in range(N):
                        if (l+m) % 3 == 0:
                            cost += D[c[l][m]-1][i]
                        elif (l+m) % 3 == 1:
                            cost += D[c[l][m]-1][j]
                        else:
                            cost += D[c[l][m]-1][k]
                ans = min(ans, cost)

    #print
    print(ans)

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
