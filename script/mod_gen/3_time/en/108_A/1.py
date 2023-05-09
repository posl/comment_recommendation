def count_pairs(k):
    if k % 2 == 0:
        return k // 2 * (k // 2)
    else:
        return k // 2 * (k // 2 + 1)

if __name__ == '__main__':
    count_pairs()