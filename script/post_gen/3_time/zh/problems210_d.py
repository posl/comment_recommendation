Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def getMinCost(h, w, c, a):
    #dp[i][j]表示在(i,j)建站的最小成本
    dp = [[0 for j in range(w)] for i in range(h)]
    #初始化
    dp[0][0] = a[0][0]
    for i in range(1, h):
        dp[i][0] = dp[i-1][0] + c*(i)
    for j in range(1, w):
        dp[0][j] = dp[0][j-1] + c*(j)
    #递推
    for i in range(1, h):
        for j in range(1, w):
            dp[i][j] = min(dp[i-1][j]+c*(i), dp[i][j-1]+c*(j), dp[i-1][j-1]+c*(i+j)) + a[i][j]
    return dp[h-1][w-1]

=======
Suggestion 3

def main():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    ans = float('inf')
    for i in range(h):
        for j in range(w):
            for i2 in range(i,h):
                for j2 in range(j+1,w):
                    ans = min(ans, a[i][j] + a[i2][j2] + c * (abs(i-i2)+abs(j-j2)))
            for i2 in range(i+1,h):
                for j2 in range(j,w):
                    ans = min(ans, a[i][j] + a[i2][j2] + c * (abs(i-i2)+abs(j-j2)))
    print(ans)

=======
Suggestion 4

def solve():
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i == i2 and j == j2:
                        continue
                    ans = min(ans, a[i][j] + a[i2][j2] + c*(abs(i-i2)+abs(j-j2)))
    print(ans)

=======
Suggestion 5

def get_min_cost(h, w, c, a):
    min_cost = 1000000000000000000
    for i in range(h):
        for j in range(w):
            for p in range(h):
                for q in range(w):
                    if i == p and j == q:
                        continue
                    cost = a[i][j] + a[p][q] + c * (abs(i - p) + abs(j - q))
                    if cost < min_cost:
                        min_cost = cost
    return min_cost

=======
Suggestion 6

def main():
    #读入数据
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    #初始化
    dp = [[float('inf')] * W for _ in range(H)]
    #动态规划
    for i in range(H):
        for j in range(W):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
            dp[i][j] = min(dp[i][j], A[i][j])
    #输出结果
    print(dp[-1][-1])

=======
Suggestion 7

def main():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    mincost = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    if i == k and j == l:
                        continue
                    cost = a[i][j] + a[k][l] + c * (abs(i-k) + abs(j-l))
                    mincost = min(mincost, cost)
    print(mincost)

=======
Suggestion 8

def main():
    #H,W,C = map(int, input().split())
    #A = [list(map(int, input().split())) for _ in range(H)]
    H,W,C = 3,4,2
    A = [[1,7,7,9],[9,6,3,7],[7,8,6,4]]
    print(H,W,C,A)
    #print([A[i][j] for i in range(H) for j in range(W)])
    #print([A[i][j] for i in range(H) for j in range(W) if i==0 or j==0])
    #print([A[i][j] for i in range(H) for j in range(W) if i==1 or j==2])
    #print([A[i][j] for i in range(H) for j in range(W) if i==2 or j==3])
    #print([A[i][j] for i in range(H) for j in range(W) if i==0 or j==0])
    #print([A[i][j] for i in range(H) for j in range(W) if i==1 or j==2])
    #print([A[i][j] for i in range(H) for j in range(W) if i==2 or j==3])
    #print([A[i][j] for i in range(H) for j in range(W) if i==0 or j==0])
    #print([A[i][j] for i in range(H) for j in range(W) if i==1 or j==2])
    #print([A[i][j] for i in range(H) for j in range(W) if i==2 or j==3])
    #print([A[i][j] for i in range(H) for j in range(W) if i==0 or j==0])
    #print([A[i][j] for i in range(H) for j in range(W) if i==1 or j==2])
    #print([A[i][j] for i in range(H) for j in range(W) if i==2 or j==3])
    #print([A[i][j] for i in range(H) for j in range(W) if i==0 or j==0])
    #print([A[i][j

=======
Suggestion 9

def main():
    h,w,c = map(int,input().split())
    A = []
    for i in range(h):
        A.append(list(map(int,input().split())))

    ans = 10**18

    for i in range(h):
        for j in range(w):
            for k in range(i,h):
                for l in range(j,w):
                    if i==k and j==l:
                        continue
                    ans = min(ans,A[i][j]+A[k][l]+c*(abs(i-k)+abs(j-l)))

    print(ans)
