def count_comma(N):
    N = str(N)
    N_len = len(N)
    cnt = 0
    for i in range(N_len):
        if i % 3 == 0 and i != 0:
            cnt += 1
    return cnt
