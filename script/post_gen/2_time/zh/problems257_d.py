Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def calc(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

=======
Suggestion 2

def solve(num, x, y, p):
    ans = 0
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            if p[i] * ans >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                ans += 1
                break
    return ans

=======
Suggestion 3

def main():
    N = int(input())
    # x = []
    # y = []
    # p = []
    # for i in range(N):
    #     x_i, y_i, p_i = map(int, input().split())
    #     x.append(x_i)
    #     y.append(y_i)
    #     p.append(p_i)
    # print(x)
    # print(y)
    # print(p)
    # for i in range(N):
    #     for j in range(N):
    #         if i == j:
    #             continue
    #         else:
    #             if p[i] * S >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
    #                 continue
    #             else:
    #                 S += 1
    # print(S)
    # print(x)
    # print(y)
    # print(p)
    # print(S)
    x = []
    y = []
    p = []
    for i in range(N):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    S = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                if p[i] * S >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                    continue
                else:
                    S += 1
    print(S)

=======
Suggestion 4

def get_distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

=======
Suggestion 5

def readinput():
    n=int(input())
    xyplist=[]
    for i in range(n):
        xyplist.append(list(map(int,input().split())))
    return n,xyplist

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    for i in range(N):
        x, y, p = map(int, input().split())
        A.append((x, y, p))
    A.sort(key=lambda x: x[0] + x[1])
    dp = [float("inf")] * (N + 1)
    dp[0] = -float("inf")
    for i in range(N):
        dp[i + 1] = min(dp[i + 1], A[i][1] - A[i][0])
        for j in range(i):
            dp[i + 1] = min(dp[i + 1], dp[j] + A[i][1] + A[i][0] - A[j][1] - A[j][0])
    return dp[N]

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(arr)

=======
Suggestion 9

def get_input():
    N = int(input())
    x = []
    y = []
    P = []
    for i in range(N):
        x_i, y_i, P_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(P_i)
    return N, x, y, P
