def comb(n, k):
    if k > n:
        return 0
    if k * 2 > n:
        k = n - k
    if k == 0:
        return 1
    result = n
    for i in range(2, k+1):
        result = result * (n - i + 1) // i
    return result
N, K = map(int, input().split())
mod = 10**9 + 7
for i in range(1, K+1):
    if i > N-K+1:
        print(0)
    else:
        print(comb(N-K+1, i) * comb(K-1, i-1) % mod)
