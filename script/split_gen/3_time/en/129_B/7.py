def main():
    N = int(input())
    W = list(map(int, input().split()))
    # Find the minimum possible absolute difference of S_1 and S_2.
    # S_1 = W_1 + W_2 + ... + W_T
    # S_2 = W_{T+1} + ... + W_N
    # S_1 - S_2 = (W_1 + ... + W_T) - (W_{T+1} + ... + W_N)
    #           = (W_1 + ... + W_T) - (W_1 + ... + W_T + W_{T+1} + ... + W_N)
    #           = (W_1 + ... + W_T) - (W_1 + ... + W_T) - (W_{T+1} + ... + W_N)
    #           = 0 - (W_{T+1} + ... + W_N)
    #           = -(W_{T+1} + ... + W_N)
    # So, we need to find the minimum of -(W_{T+1} + ... + W_N).
    # Note that W_{T+1} + ... + W_N = W_N + ... + W_{T+1}.
    # So, we need to find the minimum of -(W_N + ... + W_{T+1}).
    # We can calculate W_N + ... + W_{T+1} by using the cumulative sum.
    # So, we need to find the minimum of -cumsum[N-1] + cumsum[T].
    cumsum = [0] * N
    cumsum[0] = W[0]
    for i in range(1, N):
        cumsum[i] = cumsum[i-1] + W[i]
    ans = 10**9
    for i in range(N-1):
        ans = min(ans, abs(-cumsum[N-1] + 2*cumsum[i]))
    print(ans)
