def jump(n, x, a, b):
    i = 0
    while i < n:
        if x < a[i] or x > b[i]:
            return False
        i += 1
    return True

if __name__ == '__main__':
    jump()