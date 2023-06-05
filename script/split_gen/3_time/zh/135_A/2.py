def solve(a,b):
    if a == b:
        return a
    elif a > b:
        if (a - b) % 2 == 0:
            return (a - b) // 2
        else:
            return "IMPOSSIBLE"
    else:
        if (b - a) % 2 == 0:
            return (b - a) // 2
        else:
            return "IMPOSSIBLE"
