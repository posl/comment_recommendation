def count_sequences(N, M, K):
    #print("N=", N, " M=", M, " K=", K)
    if N == 1:
        return M
    else:
        count = 0
        for i in range(1, M+1):
            count += count_sequences(N-1, M, K-i)
        return count
N, M, K = map(int, input().split())
print(count_sequences(N, M, K) % 998244353)
