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
