def count(n, m):
    if n == 0 or m == 0:
        return 1
    return count(n - 1, m) + count(n, m - 1)

if __name__ == '__main__':
    count()