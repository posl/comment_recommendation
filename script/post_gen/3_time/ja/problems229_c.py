Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #A[i]の値が小さい順に並べ替える
    A, B = zip(*sorted(zip(A, B)))
    #Bの累積和を求める
    B_sum = [0] * (N + 1)
    for i in range(N):
        B_sum[i + 1] = B_sum[i] + B[i]
    #A[i]の値について、Bの累積和の最大値を求める
    B_sum_max = [0] * (N + 1)
    B_sum_max[N] = B_sum[N]
    for i in range(N - 1, -1, -1):
        B_sum_max[i] = max(B_sum_max[i + 1], B_sum[i + 1])
    #A[i]の値について、A[i] * B[j]の最大値を求める
    A_B_max = [0] * (N + 1)
    for i in range(N):
        A_B_max[i + 1] = max(A_B_max[i], A[i] * B[i])
    #A[i]の値について、A[i] * B[j] + B_sum[j]の最大値を求める
    A_B_B_sum_max = [0] * (N + 1)
    for i in range(N):
        A_B_B_sum_max[i + 1] = max(A_B_B_sum_max[i], A_B_max[i + 1] + B_sum_max[i + 1])
    #A[i]の値について、A[i] * B[j] + B_sum[j]がWを超えない最大値を求める
    A_B_B_sum_W_max = [0] * (N + 1)
    for i in range(N):
        if A[i] * B_sum[N] <= W:
            A_B_B_sum_W_max[i + 1] =

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [0]*(W+1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j + B[i] <= W:
                dp[j+B[i]] = max(dp[j+B[i]], dp[j] + A[i])
    print(max(dp))

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        a, b = map(int, input().split())
        cheese.append((a, b))

    cheese.sort(key=lambda x: x[0] / x[1], reverse=True)

    ans = 0
    for a, b in cheese:
        ans += a * min(W // b, 1)
        W -= b * min(W // b, 1)

    print(ans)

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1])
    ans = 0
    for i in range(N):
        if cheese[i][1] <= W:
            ans += cheese[i][0]
            W -= cheese[i][1]
        else:
            ans += cheese[i][0] * W / cheese[i][1]
            break
    print(int(ans))

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        a, b = map(int, input().split())
        cheese.append([a, b])
    cheese.sort(reverse=True)
    #print(cheese)
    dp = [0] * (W+1)
    for i in range(N):
        for j in range(W, cheese[i][1]-1, -1):
            dp[j] = max(dp[j], dp[j-cheese[i][1]] + cheese[i][0])
    print(dp[W])

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0] / x[1])
    ans = 0
    for i in range(N):
        if W == 0:
            break
        if W >= cheese[i][1]:
            W -= cheese[i][1]
            ans += cheese[i][0]
        else:
            ans += cheese[i][0] * (W / cheese[i][1])
            W = 0
    print(int(ans))

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1])
    #print(cheese)
    ans = 0
    for i in range(N):
        if W >= cheese[i][1]:
            ans += cheese[i][0]
            W -= cheese[i][1]
        else:
            ans += cheese[i][0] * W / cheese[i][1]
            break
    print(int(ans))

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    C = []
    for _ in range(N):
        a, b = map(int, input().split())
        C.append((a, b))
    C.sort()
    dp = [0] * (W + 1)
    for a, b in C:
        for w in range(W, b - 1, -1):
            dp[w] = max(dp[w], dp[w - b] + a)
    print(dp[-1])

=======
Suggestion 9

def main():
    N,W = map(int,input().split())
    cheese = []
    for i in range(N):
        cheese.append(list(map(int,input().split())))
    cheese.sort(key=lambda x:x[0]/x[1],reverse=True)
    ans = 0
    for i in range(N):
        if W == 0:
            break
        if cheese[i][1] <= W:
            ans += cheese[i][0]
            W -= cheese[i][1]
        else:
            ans += cheese[i][0] * W / cheese[i][1]
            W = 0
    print(int(ans))

=======
Suggestion 10

def main():
    n, w = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    cheese.sort(key=lambda x: x[1])
    dp = [0] * (w + 1)
    for a, b in cheese:
        for i in range(w, b - 1, -1):
            dp[i] = max(dp[i], dp[i - b] + a)
    print(dp[w])
