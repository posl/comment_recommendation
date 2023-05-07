def count_int_averages(A):
    N = len(A)
    mod = 998244353
    ans = 0
    for i in range(1, 2 ** N):
        bits = bin(i)[2:].zfill(N)
        cnt = sum([int(b) for b in bits])
        s = sum([int(bits[j]) * A[j] for j in range(N)])
        if s % cnt == 0:
            ans += 1
    return ans % mod
