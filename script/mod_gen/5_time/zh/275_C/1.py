def get_num_of_chessboard(s):
    res = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                if i + 1 < 9 and j + 1 < 9:
                    if s[i][j + 1] == '#' and s[i + 1][j] == '#' and s[i + 1][j + 1] == '#':
                        res += 1
    return res

if __name__ == '__main__':
    get_num_of_chessboard()