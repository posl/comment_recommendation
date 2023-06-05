def problem126_c(n,k):
    if n>k:
        return 1/(2**(n-k))
    else:
        return 0.5
