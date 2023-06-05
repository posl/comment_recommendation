def jump(n, x, a, b):
    if x == 0:
        return True
    if n == 0:
        return False
    return jump(n - 1, x - a[n - 1], a, b) or jump(n - 1, x - b[n - 1], a, b)

if __name__ == '__main__':
    jump()