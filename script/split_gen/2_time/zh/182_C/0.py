def solve(n):
    #n = input()
    n = int(n)
    k = len(str(n))
    if k == 1:
        return -1
    if k == 2:
        if n % 3 == 0:
            return 0
        else:
            return -1
    if k == 3:
        if n % 3 == 0:
            return 0
        else:
            return -1
    if k >= 4:
        if n % 3 == 0:
            return 0
        else:
            if n % 3 == 1:
                return 1
            else:
                return 2
