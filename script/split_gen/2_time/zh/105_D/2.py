def num_divisible_by_m(A, M):
    N = len(A)
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    #print(sum_A)
    #print(sum_A[1:])
    #print(sum_A[1:] % M)
    remainder = [x % M for x in sum_A[1:]]
    #print(remainder)
    from collections import Counter
    c = Counter(remainder)
    #print(c)
    ans = 0
    for k, v in c.items():
        ans += v * (v - 1) // 2
    return ans
