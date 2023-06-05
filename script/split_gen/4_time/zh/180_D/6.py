def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X <= Y // A and X * A < X + B:
        X *= A
        exp += 1
    exp += (Y - 1 - X) // B
    print(exp)
