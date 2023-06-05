def get_all_cover(H, W, A, B):
    if A == 0 and B == 0:
        return 1
    elif A == 0:
        return get_all_cover(W, H, B, A)
    elif W == 1:
        return 1
    elif W == 2:
        return 2
    elif W == 3:
        return 3
    elif W == 4:
        return 4
    elif W == 5:
        return 5
    else:
        if A == 0:
            return get_all_cover(H, W-2, A, B-1) + get_all_cover(H, W-1, A, B-1)
        else:
            return get_all_cover(H, W-2, A-1, B) + get_all_cover(H, W-1, A-1, B) + get_all_cover(H, W-2, A, B-1) + get_all_cover(H, W-1, A, B-1)
