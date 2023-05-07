def get_tile_num(H, W, A, B):
    if H == 1 and W == 1:
        return 1
    if W == 1:
        return get_tile_num(H-1, W, B, A)
    if A == 0:
        return 1
    if H == 1:
        return get_tile_num(H, W-1, A-1, B)
    return get_tile_num(H-1, W, B, A) + get_tile_num(H, W-1, A-1, B)

if __name__ == '__main__':
    get_tile_num()