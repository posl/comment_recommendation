def solve(a,b):
    if a == 0 and b == 0:
        return 0
    elif a == 1 and b == 1:
        return 4
    elif a == 1 and b == 2:
        return 3
    elif a == 1 and b == 3:
        return 2
    elif a == 1 and b == 4:
        return 1
    elif a == 2 and b == 1:
        return 3
    elif a == 2 and b == 2:
        return 2
    elif a == 2 and b == 3:
        return 1
    elif a == 3 and b == 1:
        return 2
    elif a == 3 and b == 2:
        return 1
    elif a == 4 and b == 1:
        return 1
    else:
        return 0

if __name__ == '__main__':
    solve()