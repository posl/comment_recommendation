def get_num(N, M, K):
    if N == 1:
        return 1
    if N == 2:
        return M
    if N == 3:
        return M * (M + 1) / 2
    if N == 4:
        return M * (M + 1) * (M + 2) / 6
    if N == 5:
        return M * (M + 1) * (M + 2) * (M + 3) / 24
    if N == 6:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) / 120
    if N == 7:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) / 720
    if N == 8:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) / 5040
    if N == 9:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) * (M + 7) / 40320
    if N == 10:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) * (M + 7) * (M + 8) / 362880
    if N == 11:
        return M * (M + 1) * (M + 2) * (M + 3) * (M + 4) * (M + 5) * (M + 6) * (M + 7) * (M + 8) * (M + 9) / 3628800
    if N == 12:
        return M * (M + 1) * (M + 2
