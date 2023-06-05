def get_num_of_square(S):
    count = 0
    for r in range(1, 9):
        for c in range(1, 9):
            if S[r][c] == '#':
                if S[r - 1][c - 1] == '#' and S[r - 1][c] == '#' and S[r][c - 1] == '#':
                    count += 1
    return count
