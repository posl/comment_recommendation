def solve(n):
    if n < 1000:
        return 0
    else:
        s = str(n)
        if len(s) % 3 == 0:
            return len(s) // 3 - 1
        else:
            return len(s) // 3
