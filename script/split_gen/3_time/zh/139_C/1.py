def max_move(n, h):
    max_move = 0
    for i in range(0, n):
        move = 1
        for j in range(i, n-1):
            if h[j] <= h[j+1]:
                move += 1
            else:
                break
        if move > max_move:
            max_move = move
    return max_move
