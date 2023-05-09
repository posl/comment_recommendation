def solve(N, W):
    # Write your code here
    #print(N, W)
    W.sort()
    #print(N, W)
    sum1 = 0
    sum2 = 0
    for i in range(N):
        if i < N//2:
            sum1 += W[i]
        else:
            sum2 += W[i]
    #print(sum1, sum2)
    return abs(sum1-sum2)
