def solve(N, K, P, C):
    ans = -10**18
    for i in range(N):
        j = P[i] - 1
        k = 0
        score = 0
        while j != i and k < K:
            score += C[j]
            ans = max(ans, score)
            j = P[j] - 1
            k += 1
        if k < K:
            l = min(K, K - (K - k) % (k + 1))
            if score > 0:
                ans = max(ans, score * (K // (k + 1)) + max(score * (l // (k + 1)), score + max(score * ((l - k - 1) // (k + 1)), 0)))
            else:
                ans = max(ans, score * (K // (k + 1)) + max(score * (l // (k + 1)), score + max(score * ((l - k - 1) // (k + 1)), 0)), score * (K // (k + 1)) + max(score * (l // (k + 1)), score + max(score * ((l - k - 1) // (k + 1)), 0)))
    return ans

if __name__ == '__main__':
    solve()