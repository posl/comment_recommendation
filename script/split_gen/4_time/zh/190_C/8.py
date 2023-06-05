def solve(N, M, AB, K, CD):
    ans = 0
    for i in range(2**K):
        balls = [0] * N
        for j in range(K):
            if (i >> j) & 1:
                balls[CD[j][0]-1] += 1
            else:
                balls[CD[j][1]-1] += 1
        cnt = 0
        for a, b in AB:
            if balls[a-1] and balls[b-1]:
                cnt += 1
        ans = max(ans, cnt)
    return ans
