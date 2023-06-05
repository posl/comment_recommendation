def solve(n, a):
    if n == 1:
        if a[0] == 1:
            return [1]
        else:
            return [-1]
    if n == 2:
        if a[0] == 0 and a[1] == 0:
            return [0]
        elif a[0] == 1 and a[1] == 1:
            return [1, 2]
        else:
            return [-1]
    if n == 3:
        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            return [0]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0:
            return [1]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0:
            return [2]
        elif a[0] == 0 and a[1] == 0 and a[2] == 1:
            return [3]
        elif a[0] == 1 and a[1] == 1 and a[2] == 0:
            return [1, 2]
        elif a[0] == 0 and a[1] == 1 and a[2] == 1:
            return [2, 3]
        elif a[0] == 1 and a[1] == 0 and a[2] == 1:
            return [1, 3]
        elif a[0] == 1 and a[1] == 1 and a[2] == 1:
            return [1, 2, 3]
        else:
            return [-1]
    if n == 4:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            return [0]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            return [1]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 0:
            return [2

if __name__ == '__main__':
    solve()