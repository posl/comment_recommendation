Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    C = [0] * N
    A = [0] * N
    for i in range(N):
        if S[i] == '0':
            C[i] = 1
        else:
            A[i] = 1
    for i in range(1, N):
        C[i] += C[i-1]
        A[i] += A[i-1]
    ans = 0
    for i in range(N):
        ans = max(ans, C[i] + A[N-1] - A[i])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W_0 = []
    W_1 = []
    for i in range(N):
        if S[i] == '0':
            W_0.append(W[i])
        else:
            W_1.append(W[i])
    W_0.sort()
    W_1.sort()
    W_0.append(10**9+1)
    W_1.append(10**9+1)
    W_0 = W_0 + [0] * len(W_1)
    W_1 = W_1 + [0] * len(W_0)
    ans = 0
    i_0 = 0
    i_1 = 0
    for i in range(N):
        if S[i] == '0':
            if W_1[i_1] < W_0[i_0]:
                ans += 1
                i_1 += 1
            else:
                i_0 += 1
        else:
            if W_0[i_0] < W_1[i_1]:
                ans += 1
                i_0 += 1
            else:
                i_1 += 1
    print(ans)

=======
Suggestion 3

def read_input():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    return N, S, W

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    if ans == 0:
        print(N)
    elif ans == 1:
        print(N-1)
    else:
        print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W.sort()
    ans = 0
    for x in range(1, N+1):
        if S[x-1] == '1':
            ans += N-x+1
        else:
            ans += x
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))

    # 0: child, 1: adult
    s = [int(x) for x in s]

    # 0: child, 1: adult
    w = [(x, i) for i, x in enumerate(w)]
    w.sort()

    # 0: child, 1: adult
    s = [s[x[1]] for x in w]

    # 0: child, 1: adult
    c = [0] * n
    a = [0] * n

    # 0: child, 1: adult
    c[0] = 1 - s[0]
    a[0] = s[0]

    for i in range(1, n):
        c[i] = c[i - 1] + 1 - s[i]
        a[i] = a[i - 1] + s[i]

    ans = 0
    for i in range(n):
        ans = max(ans, c[i] + a[n - 1] - a[i])

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    W = [int(x) for x in input().split()]
    W = W[::-1]
    S = S[::-1]
    #print(N, S, W)
    left = 0
    right = 10**9
    while right - left > 1:
        #print(left, right)
        mid = (left + right) // 2
        if check(mid, N, S, W):
            left = mid
        else:
            right = mid
    if check(right, N, S, W):
        print(right)
    else:
        print(left)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)

    # 0: child, 1: adult
    # 0: left, 1: right
    # 0: max, 1: min
    # 0: # of children, 1: # of adults
    dp = [[[[-1, -1], [-1, -1]] for _ in range(2)] for _ in range(N+1)]

    # dp[i][j][k][l][m] = max number of people Takahashi can judge correctly
    # when he uses X = W[i] as a threshold and he judges the people from
    # W[0] to W[i-1] correctly
    # j = 0: W[i] is a child
    # j = 1: W[i] is an adult
    # k = 0: W[i] is on the left side of the threshold
    # k = 1: W[i] is on the right side of the threshold
    # l = 0: W[i] is the maximum weight among the people on the left side of the threshold
    # l = 1: W[i] is the minimum weight among the people on the left side of the threshold
    # m = 0: # of children on the left side of the threshold
    # m = 1: # of adults on the left side of the threshold

    # base case
    dp[0][0][0][0][0] = 0
    dp[0][1][1][0][0] = 0

    for i in range(1, N+1):
        # W[i] is a child
        if S[i-1] == '0':
            # W[i] is on the left side of the threshold
            # W[i] is the maximum weight among the people on the left side of the threshold
            # # of children on the left side of the threshold increases by 1
            dp[i][0][0][0][0] = max(dp[i-1][0][0][0][0], dp[i-1][0][0][1][0]) + 1
            # W[i] is the

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    # 0以上N未満の整数iについて、W[i]の値がX以上であるようなXの個数を数える
    for i in range(N):
        if S[i] == '1':
            ans += len([x for x in W[i:] if x >= W[i]])
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)
    #print(len(S), len(W))
    #print(S[0:1])
    #print(W[0:1])
    #print(W[0:2])
    #print(W[0:3])
    #print(W[0:4])
    #print(W[0:5])
    #print(W[0:6])
    #print(W[0:7])
    #print(W[0:8])
    #print(W[0:9])
    #print(W[0:10])
    #print(W[0:11])
    #print(W[0:12])
    #print(W[0:13])
    #print(W[0:14])
    #print(W[0:15])
    #print(W[0:16])
    #print(W[0:17])
    #print(W[0:18])
    #print(W[0:19])
    #print(W[0:20])
    #print(W[0:21])
    #print(W[0:22])
    #print(W[0:23])
    #print(W[0:24])
    #print(W[0:25])
    #print(W[0:26])
    #print(W[0:27])
    #print(W[0:28])
    #print(W[0:29])
    #print(W[0:30])
    #print(W[0:31])
    #print(W[0:32])
    #print(W[0:33])
    #print(W[0:34])
    #print(W[0:35])
    #print(W[0:36])
    #print(W[0:37])
    #print(W[0:38])
    #print(W[0:39])
    #print(W[0:40])
    #print(W[0:41])
    #print(W[0:42])
    #print(W[0:43])
    #print(W[0:44])
    #print(W[0:45])
    #print(W[0:46])
    #print(W[0:47])
    #print(W[0:48])
    #print(W[0:49])
    #print(W[0:50
