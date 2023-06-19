def get_all_weight(w):
    if w <= 3:
        return [w]
    if w <= 6:
        return [1, w-1]
    if w <= 9:
        return [2, w-2]
    if w <= 12:
        return [3, w-3]
    if w <= 15:
        return [1, 2, w-3]
    if w <= 18:
        return [1, 3, w-4]
    if w <= 21:
        return [2, 3, w-5]
    return [1, 2, 3, w-6]
