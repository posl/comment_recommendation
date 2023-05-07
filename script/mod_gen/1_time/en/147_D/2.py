def solve(N, A):
    # mod = 10**9 + 7
    # ans = 0
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         ans += A[i] ^ A[j]
    #         ans %= mod
    # return ans
    # print(A)
    mod = 10**9 + 7
    ans = 0
    for i in range(60):
        # print("i", i)
        count = 0
        for j in range(N):
            if A[j] & 1:
                count += 1
            A[j] >>= 1
        # print("count", count)
        ans += count * (N-count) * pow(2, i, mod)
        ans %= mod
    return ans

if __name__ == '__main__':
    solve()