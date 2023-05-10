def get_max_books(n, m, k, a, b):
    if n == 0 or m == 0:
        return 0
    if a[0] > k and b[0] > k:
        return 0
    if a[0] > k:
        return get_max_books(n, m-1, k, a, b[1:])
    if b[0] > k:
        return get_max_books(n-1, m, k, a[1:], b)
    return 1 + max(get_max_books(n, m-1, k-b[0], a, b[1:]), get_max_books(n-1, m, k-a[0], a[1:], b))

if __name__ == '__main__':
    get_max_books()