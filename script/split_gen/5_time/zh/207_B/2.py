def solve(a, b, c, d):
    if a < b:
        return -1
    if d * c < b:
        return -1
    if d == 1:
        return 0
    ans = (a * d - b + c - 1) // (c - b)
    return ans
