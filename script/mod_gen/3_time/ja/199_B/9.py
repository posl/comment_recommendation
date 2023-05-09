def count_x(n, a, b):
    x = 0
    for i in range(n):
        x = max(x, a[i])
    for i in range(n):
        x = min(x, b[i])
    return x

if __name__ == '__main__':
    count_x()