def solve(X, Y, A, B):
    exp = 0
    while X * A < X + B and X * A < Y:
        X *= A
        exp += 1
    return exp + (Y - X - 1) // B
