def check(lst):
    count = 0
    for i in range(H):
        for j in range(W):
            if lst[i][j] == '#':
                count += 1
    if count == K:
        return True
    else:
        return False
