def get_next(seq, n, m):
    if len(seq) == n:
        print(*seq)
    else:
        for i in range(seq[-1]+1, m+1):
            get_next(seq+[i], n, m)
