def get_median(l: list) -> int:
    l = sorted(l)
    return l[(len(l) - 1) // 2]

if __name__ == '__main__':
    get_median()