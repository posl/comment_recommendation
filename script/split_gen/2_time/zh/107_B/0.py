def problems107_b(H, W, a):
    result = []
    for i in range(H):
        result.append([])
        for j in range(W):
            result[i].append('.')
    for i in range(H):
        for j in range(W):
            if a[i][j] == '#':
                for k in range(W):
                    result[i][k] = '#'
                for k in range(H):
                    result[k][j] = '#'
    return result
