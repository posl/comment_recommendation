def solve(X, Y, A, B):
    exp = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            exp += 1
        else:
            exp += (Y - X - 1) // B
            break
    return exp
