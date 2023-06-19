def get_max_M(N):
    if N == 1:
        return 0
    if N == 2:
        return 1
    if N % 2 == 0:
        return int(N / 2) * int(N / 2)
    else:
        return int(N / 2) * int(N / 2 + 1)
