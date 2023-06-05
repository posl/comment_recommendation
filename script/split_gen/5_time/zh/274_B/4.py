def get_x_list(h, w, c_list):
    x_list = []
    for j in range(w):
        x = 0
        for i in range(h):
            if c_list[i][j] == '#':
                x += 1
        x_list.append(x)
    return x_list
