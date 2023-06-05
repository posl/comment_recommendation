def exchange(a, b, c, d, e):
    for i in range(b-1, c):
        a[i], a[d+i-c+1] = a[d+i-c+1], a[i]
    return a

if __name__ == '__main__':
    exchange()