def solve(w):
    if w <= 3:
        return [w]
    if w % 2 == 0:
        return [2] + solve(w - 2)
    else:
        return [3] + solve(w - 3)
