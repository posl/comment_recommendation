def get_pyramid_center_and_height(N, x, y, h):
    for cx in range(101):
        for cy in range(101):
            H = h[0] + abs(x[0] - cx) + abs(y[0] - cy)
            if H > 0:
                for i in range(1, N):
                    if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                        break
                else:
                    return cx, cy, H
    return None, None, None

if __name__ == '__main__':
    get_pyramid_center_and_height()