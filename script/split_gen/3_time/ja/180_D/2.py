def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y and X * A < X + B:
        X *= A
        exp += 1
    exp += (Y - X - 1) // B
    print(exp)
