def reverse_string(L, R, S):
    return S[:L-1] + S[L-1:R][::-1] + S[R:]
