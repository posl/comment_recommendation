def transpose_matrix(a, h, w):
    for i in range(w):
        for j in range(h):
            print(a[j][i], end='')
            if j < h-1:
                print(' ', end='')
        print('')
