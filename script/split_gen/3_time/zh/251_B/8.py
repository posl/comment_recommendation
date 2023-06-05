def count_good_number(n, w, a):
    a.sort()
    if a[0] > w:
        return 0
    if n == 1:
        return 1
    if n == 2:
        if a[0] + a[1] <= w:
            return 3
        else:
            return 2
    if n == 3:
        if a[0] + a[1] + a[2] <= w:
            return 7
        elif a[0] + a[1] <= w:
            return 6
        elif a[0] + a[2] <= w:
            return 6
        elif a[1] + a[2] <= w:
            return 6
        else:
            return 5
    if n == 4:
        if a[0] + a[1] + a[2] + a[3] <= w:
            return 15
        elif a[0] + a[1] + a[2] <= w:
            return 14
        elif a[0] + a[1] + a[3] <= w:
            return 14
        elif a[0] + a[2] + a[3] <= w:
            return 14
        elif a[1] + a[2] + a[3] <= w:
            return 14
        elif a[0] + a[1] <= w:
            return 13
        elif a[0] + a[2] <= w:
            return 13
        elif a[0] + a[3] <= w:
            return 13
        elif a[1] + a[2] <= w:
            return 13
        elif a[1] + a[3] <= w:
            return 13
        elif a[2] + a[3] <= w:
            return 13
        else:
            return 12
    if n == 5:
        if a[0] + a[1] + a[2] + a[3] + a[4] <= w:
            return 31
        elif a[0] + a[1] + a[2] + a[3] <= w:
            return 30
        elif a[0] +
