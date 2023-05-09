def solve(A, B):
    import math
    g = 1
    t = 0
    while True:
        t += A / (g ** 0.5)
        if g + B > A:
            t += A / ((g + B) ** 0.5)
            break
        else:
            g += B
    return t
