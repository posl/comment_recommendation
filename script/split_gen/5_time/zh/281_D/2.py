def solve(N, K, D, A):
    ans = -1
    for i in range(N - K + 1):
        sum = 0
        for j in range(K):
            sum += A[i + j]
        if sum % D != 0:
            ans = sum
            break
    return ans
