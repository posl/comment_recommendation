def get_median(l: list) -> int:
    l = sorted(l)
    return l[(len(l) - 1) // 2]
