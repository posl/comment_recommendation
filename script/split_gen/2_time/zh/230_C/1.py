def print_grid(n, a, b, p, q, r, s):
    for i in range(p, q+1):
        for j in range(r, s+1):
            if (i-a) == (j-b) or (i-a) == -(j-b):
                print('#', end='')
            else:
                print('.', end='')
        print()
