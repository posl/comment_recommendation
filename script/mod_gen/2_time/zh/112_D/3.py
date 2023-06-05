def func(N, x, y, h):
    for C_X in range(101):
        for C_Y in range(101):
            H = h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y)
            if H > 0:
                break
        if H > 0:
            break
    for i in range(N):
        if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
            return False
    return C_X, C_Y, H

if __name__ == '__main__':
    func()