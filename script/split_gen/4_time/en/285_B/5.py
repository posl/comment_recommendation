def get_max_non_negative_integer(S):
    N = len(S)
    max_non_negative_integer = [0] * (N-1)
    for i in range(N-1):
        l = 0
        while i + l + 1 < N:
            if S[l] != S[i + l + 1]:
                l += 1
            else:
                break
        max_non_negative_integer[i] = l
    return max_non_negative_integer
