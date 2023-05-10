def solve(K):
    ans = 0
    for i in range(1, K+1):
        for j in range(i+1, K+1):
            if i%2 != j%2:
                ans += 1
    return ans
