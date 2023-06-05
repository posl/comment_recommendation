def solve(W):
    if W <= 2:
        return [W]
    if W <= 4:
        return [1, W - 1]
    if W <= 6:
        return [1, 2, W - 3]
    if W <= 8:
        return [1, 2, 5, W - 8]
    if W <= 10:
        return [1, 2, 5, 2, W - 10]
    if W <= 12:
        return [1, 2, 5, 2, 2, W - 12]
    if W <= 14:
        return [1, 2, 5, 2, 2, 2, W - 14]
    if W <= 16:
        return [1, 2, 5, 2, 2, 2, 2, W - 16]
    if W <= 18:
        return [1, 2, 5, 2, 2, 2, 2, 2, W - 18]
    if W <= 20:
        return [1, 2, 5, 2, 2, 2, 2, 2, 2, W - 20]
    if W <= 22:
        return [1, 2, 5, 2, 2, 2, 2, 2, 2, 2, W - 22]
    if W <= 24:
        return [1, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, W - 24]
    if W <= 26:
        return [1, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, W - 26]
    if W <= 28:
        return [1, 2, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, W - 28]
    if W <= 30:
        return [1, 2, 5, 2, 2, 2, 2,

if __name__ == '__main__':
    solve()