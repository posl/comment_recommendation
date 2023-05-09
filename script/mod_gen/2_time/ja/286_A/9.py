def swap_array(a, b, c, d, e):
    for i in range(0, e):
        if i >= b and i <= c:
            a[i], a[d+i-b] = a[d+i-b], a[i]
    return a

if __name__ == '__main__':
    swap_array()