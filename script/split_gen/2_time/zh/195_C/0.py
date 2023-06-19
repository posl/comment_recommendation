def solve(N):
    N_str = str(N)
    N_len = len(N_str)
    if N_len <= 3:
        return 0
    elif N_len <= 6:
        return N_len - 3
    elif N_len <= 9:
        return N_len - 3 + (N_len - 3) // 3
    elif N_len <= 12:
        return N_len - 3 + (N_len - 3) // 3 + (N_len - 6) // 3
    elif N_len <= 15:
        return N_len - 3 + (N_len - 3) // 3 + (N_len - 6) // 3 + (N_len - 9) // 3
    else:
        return N_len - 3 + (N_len - 3) // 3 + (N_len - 6) // 3 + (N_len - 9) // 3 + (N_len - 12) // 3
