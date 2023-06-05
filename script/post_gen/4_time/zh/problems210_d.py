Synthesizing 10/10 solutions

=======
Suggestion 1

def read_data():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    return h, w, c, a

=======
Suggestion 2

def min_cost():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18

    for _ in range(2):
        dp = [[10**18] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                    ans = min(ans, dp[i-1][j] + C + A[i][j] + C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
                    ans = min(ans, dp[i][j-1] + C + A[i][j] + C)
                dp[i][j] = min(dp[i][j], A[i][j])
    print(ans)

min_cost()

=======
Suggestion 3

def main():
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    min_cost = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(i+1, h):
                for l in range(j+1, w):
                    min_cost = min(min_cost, a[i][j]+a[k][l]+c*(abs(i-k)+abs(j-l)))
    print(min_cost)

=======
Suggestion 4

def main():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = float('inf')
    for i in range(h):
        for j in range(w):
            for k in range(i, h):
                for l in range(j, w):
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i - k) + abs(j - l)))
    print(ans)

=======
Suggestion 5

def get_min_cost(h, w, c, a):
    min_cost = 10**9 * 10**9
    # 从左上角开始遍历
    for i in range(h):
        for j in range(w):
            # 从右下角开始遍历
            for k in range(h-1, i-1, -1):
                for l in range(w-1, j-1, -1):
                    # 计算建站花费
                    cost = a[i][j] + a[k][l]
                    # 计算建轨道花费
                    cost += c * (abs(i-k) + abs(j-l))
                    min_cost = min(min_cost, cost)
    return min_cost

=======
Suggestion 6

def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))

    min_cost = 10 ** 18
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(W):
                    cost = A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l))
                    if i == k and j == l:
                        continue
                    min_cost = min(min_cost, cost)

    print(min_cost)

=======
Suggestion 7

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18] * (w + 1) for _ in range(h + 1)]
        for i in range(h):
            for j in range(w):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + c
                ans = min(ans, dp[i + 1][j + 1] + a[i][j])
        a = a[::-1]
    print(ans)

=======
Suggestion 8

def main():
    h,w,c=map(int,input().split())
    a=[]
    for i in range(h):
        a.append(list(map(int,input().split())))
    min_cost=10**18
    for i in range(h):
        for j in range(w):
            for k in range(i,h):
                for l in range(j,w):
                    cost=a[i][j]+a[k][l]+c*(abs(i-k)+abs(j-l))
                    if cost<min_cost:
                        min_cost=cost
    print(min_cost)

=======
Suggestion 9

def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_cost = float('inf')
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    cost = A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l))
                    min_cost = min(min_cost, cost)
    print(min_cost)

=======
Suggestion 10

def solve(h, w, c, a):
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i == i2 and j == j2:
                        continue
                    cost = a[i][j] + a[i2][j2] + c * (abs(i - i2) + abs(j - j2))
                    ans = min(ans, cost)
    return ans
