def problem126_c(N, K):
    if N >= K:
        return 1
    elif N == 1:
        return 1 / K
    else:
        return (1 / N) * (1 / 2) ** (len(bin(K - 1)) - 2)
