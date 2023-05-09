def count_coma(h, w, s):
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                count += 1
    return count
