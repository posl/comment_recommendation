def jump(x, n, a, b):
    if n == 0:
        return False
    if x == 0:
        return True
    if x < 0:
        return False
    return jump(x-a[0], n-1, a[1:], b[1:]) or jump(x-b[0], n-1, a[1:], b[1:])

if __name__ == '__main__':
    jump()