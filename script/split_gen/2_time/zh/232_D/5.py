def func(h, w, arr):
    if h == 1 and w == 1:
        return 1
    if arr[0][1] == '#':
        if arr[1][0] == '#':
            return 0
        else:
            return 1
    if arr[1][0] == '#':
        if arr[0][1] == '#':
            return 0
        else:
            return 1
    if arr[1][1] == '#':
        return 2
    return 3
