def solve(n, s):
    r, g, b = 0, 0, 0
    for i in range(n):
        if s[i] == "R":
            r += 1
        elif s[i] == "G":
            g += 1
