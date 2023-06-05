def get_max_step(h, w, s):
    max_step = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                max_step = max(max_step, get_max_step_from_point(h, w, s, i, j))
    return max_step
