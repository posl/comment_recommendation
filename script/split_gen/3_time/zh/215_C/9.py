def get_permutation(S, K):
    # print(S, K)
    if len(S) == 1:
        return S
    else:
        n = len(S)
        p = 1
        for i in range(1, n):
            p *= i
        q = K // p
        r = K % p
        if r == 0:
            q -= 1
            r = p
        return S[q] + get_permutation(S[:q] + S[q + 1:], r)
