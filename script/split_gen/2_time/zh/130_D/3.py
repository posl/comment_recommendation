def split_rect(W, H, x, y):
    # print(W, H, x, y)
    area = W * H
    if W / 2 == x and H / 2 == y:
        return area / 2, 1
    elif W / 2 == x:
        return max(y * W, (H - y) * W), 0
    elif H / 2 == y:
        return max(x * H, (W - x) * H), 0
    else:
        return max(x * H, (W - x) * H), 0
