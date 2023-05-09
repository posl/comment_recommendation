def main():
    X, Y, A, B = map(int, input().split())
    EXP = 0
    while X * A < Y and X * A < X + B:
        X *= A
        EXP += 1
    EXP += (Y - X - 1) // B
    print(EXP)
