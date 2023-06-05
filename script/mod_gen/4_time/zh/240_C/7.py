def is_reach(x, a, b, n):
    if n == 0:
        return False
    if x == a[n-1] or x == b[n-1]:
        return True
    return is_reach(x - a[n-1], a, b, n-1) or is_reach(x - b[n-1], a, b, n-1)

if __name__ == '__main__':
    is_reach()