def print_seq(n,m):
    if n == 1:
        return [[i] for i in range(1,m+1)]
    else:
        return [[i]+j for i in range(1,m+1) for j in print_seq(n-1,m) if i > j[0]]
