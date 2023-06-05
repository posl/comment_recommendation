def get_square_count(S):
    count = 0
    for r in range(1, 8):
        for c in range(1, 8):
            if S[r][c] == "#" and S[r-1][c-1] == "#" and S[r-1][c] == "#" and S[r][c-1] == "#":
                count += 1
    return count
