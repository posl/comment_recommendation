def solve(N, K, S):
    ans = 0
    for i in range(2 ** 26):
        cnt = 0
        for j in range(N):
            for k in range(26):
                if (((i >> k) & 1) == 1) and (chr(97 + k) in S[j]):
                    cnt += 1
                    break
        if cnt == K:
            ans = max(ans, bin(i).count("1"))
    return ans
