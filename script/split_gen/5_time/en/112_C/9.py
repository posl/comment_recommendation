def getCenterAndHeight(n, x, y, h):
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                if h[i] != 0:
                    break
                if h[i] == max(h[i] + abs(x[i] - cx) + abs(y[i] - cy), 0):
                    continue
                else:
                    break
            else:
                return cx, cy, h[i] + abs(x[i] - cx) + abs(y[i] - cy)
    return None, None, None
