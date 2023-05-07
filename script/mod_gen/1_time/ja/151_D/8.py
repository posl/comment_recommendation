def get_max_move_count(h, w, s):
    max_move_count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            move_count = 0
            for k in range(h):
                for l in range(w):
                    if s[k][l] == '#':
                        continue
                    move_count = max(move_count, abs(i - k) + abs(j - l))
            max_move_count = max(max_move_count, move_count)
    return max_move_count

if __name__ == '__main__':
    get_max_move_count()