def get_weight(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 2, 3]
    if n % 2 == 0:
        return get_weight(n-1) + [n]
    else:
        return get_weight(n-2) + [n]

if __name__ == '__main__':
    get_weight()