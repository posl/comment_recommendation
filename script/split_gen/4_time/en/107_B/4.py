def problems107_b():
    H, W = map(int, input().split())
    a = [list(input()) for _ in range(H)]
    for i in range(H):
        if a[i].count('.') == W:
            a[i] = []
    for j in range(W):
        if [a[i][j] for i in range(H)].count('.') == H:
            for i in range(H):
                a[i][j] = ''
    for i in range(H):
        if a[i]:
            print(''.join(a[i]))
