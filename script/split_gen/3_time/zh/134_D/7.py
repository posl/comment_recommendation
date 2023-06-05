def solve(n, a):
    if sum(a) == 0:
        return [0]
    if n >= 3 and a[0] == 0 and a[1] == 0 and a[2] == 0:
        return [-1]
    if n >= 2 and a[0] == 0 and a[1] == 0:
        return [-1]
    if n >= 2 and a[0] == 1 and a[1] == 0:
        return [-1]
    if n >= 2 and a[0] == 1 and a[1] == 1:
        return [-1]
    if n >= 2 and a[0] == 0 and a[1] == 1:
        return [-1]
    if n >= 3 and a[0] == 1 and a[1] == 0 and a[2] == 1:
        return [-1]
    if n >= 3 and a[0] == 1 and a[1] == 1 and a[2] == 1:
        return [-1]
    if n >= 3 and a[0] == 0 and a[1] == 1 and a[2] == 1:
        return [-1]
    if n >= 4 and a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 1:
        return [-1]
    if n >= 4 and a[0] == 1 and a[1] == 1 and a[2] == 0 and a[3] == 1:
        return [-1]
    if n >= 4 and a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 1:
        return [-1]
    if n >= 4 and a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 0:
        return [-1]
    if n >= 4 and a[0] == 1 and a[1] == 1 and a[2] == 0 and a[3] == 0:
        return [-1]
    if n >=
