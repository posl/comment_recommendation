def get_second_place(n, a):
    if n == 1:
        return min(a[0], a[1])
    else:
        h = 2**(n-1)
        if a[0:h] > a[h:]:
            return get_second_place(n-1, a[0:h])
        else:
            return get_second_place(n-1, a[h:])
