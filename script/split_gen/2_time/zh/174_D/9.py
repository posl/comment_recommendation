def solve():
    n = int(input())
    s = input()
    r = s.count("R")
    w = s.count("W")
    if r == 0 or w == 0:
        return 0
    if r == w:
        return 0
    if r > w:
        return w
    else:
        return r
print(solve())
