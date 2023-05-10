def solve(n):
    if n < 9:
        return n
    if n == 9:
        return 15
    if n == 10:
        return 16
    if n == 11:
        return 17
    # n >= 12
    # (a,b) = (1, n-1)
    if n <= 16:
        return 18
    # n >= 17
    # (a,b) = (2, n-2)
    if n <= 24:
        return 19
    # n >= 25
    # (a,b) = (3, n-3)
    if n <= 36:
        return 20
    # n >= 37
    # (a,b) = (4, n-4)
    if n <= 52:
        return 21
    # n >= 53
    # (a,b) = (5, n-5)
    if n <= 72:
        return 22
    # n >= 73
    # (a,b) = (6, n-6)
    if n <= 96:
        return 23
    # n >= 97
    # (a,b) = (7, n-7)
    if n <= 124:
        return 24
    # n >= 125
    # (a,b) = (8, n-8)
    if n <= 156:
        return 25
    # n >= 157
    # (a,b) = (9, n-9)
    if n <= 192:
        return 26
    # n >= 193
    # (a,b) = (10, n-10)
    if n <= 232:
        return 27
    # n >= 233
    # (a,b) = (11, n-11)
    if n <= 276:
        return 28
    # n >= 277
    # (a,b) = (12, n-12)
    if n <= 324:
        return 29
    # n >= 325
    # (a,b) = (13, n-13)
    if n <= 376:
        return 30
    # n >= 377
    # (a,b) = (14, n-14)

if __name__ == '__main__':
    solve()