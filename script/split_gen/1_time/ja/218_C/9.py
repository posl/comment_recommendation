def rotate(S):
    return ["".join([S[r][c] for r in range(N)]) for c in range(N-1,-1,-1)]
