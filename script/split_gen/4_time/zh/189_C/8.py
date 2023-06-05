def solve(N, A):
    max_A = max(A)
    max_A_index = A.index(max_A)
    max_A_r = A[max_A_index:]
    max_A_l = A[:max_A_index + 1]
    max_A_l.reverse()
    max_A_l_index = max_A_l.index(max_A)
    max_A_r_index = max_A_r.index(max_A)
    return max_A * (max_A_l_index + max_A_r_index + 1)
