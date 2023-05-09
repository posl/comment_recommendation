def get_jewels(N, X, Y):
    if N == 1:
        return 0
    if N == 2:
        return X
    if N == 3:
        return X + Y
    return get_jewels(N-1, X, Y) + get_jewels(N-2, X, Y) + X + Y

if __name__ == '__main__':
    get_jewels()