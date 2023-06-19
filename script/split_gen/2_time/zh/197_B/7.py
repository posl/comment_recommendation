def get_visible_count(h, w, x, y, s):
    visible_count = 1
    for i in range(x-1, -1, -1):
        if s[i][y-1] == '#':
            break
        visible_count += 1
    for i in range(x, h):
        if s[i][y-1] == '#':
            break
        visible_count += 1
    for j in range(y-1, -1, -1):
        if s[x-1][j] == '#':
            break
        visible_count += 1
    for j in range(y, w):
        if s[x-1][j] == '#':
            break
        visible_count += 1
    return visible_count
