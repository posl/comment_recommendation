def rec(i, j):
    if i == 0:
        if j == 0:
            return True
        else:
            return False
    if rec(i-1, j):
        return True
    if rec(i-1, j-a[i-1]):
        return True
    return False

if __name__ == '__main__':
    rec()