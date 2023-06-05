def count_x(a, b):
    x = 0
    for i in range(len(a)):
        if a[i] > x:
            x = a[i]
        if b[i] < x:
            x = b[i]
    return x

if __name__ == '__main__':
    count_x()