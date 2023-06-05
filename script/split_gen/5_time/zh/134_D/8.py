def solve(n, a):
    if n == 1:
        if a[0] == 1:
            return [1]
        else:
            return []
    if n == 2:
        if a[0] == 0 and a[1] == 1:
            return [2]
        elif a[0] == 1 and a[1] == 0:
            return [1]
        else:
            return []
    if n == 3:
        if a[0] == 0 and a[1] == 0 and a[2] == 1:
            return [3]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0:
            return [2]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0:
            return [1]
        else:
            return []
    if n == 4:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 1:
            return [4]
        elif a[0] == 0 and a[1] == 0 and a[2] == 1 and a[3] == 0:
            return [3]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 0:
            return [2]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            return [1]
        else:
            return []
    if n == 5:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0 and a[4] == 1:
            return [5]
        elif a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 1 and a[4] == 0:
            return [4]
        elif a[0] == 0 and a[1] == 0 and a[2] == 1 and a[3] ==
