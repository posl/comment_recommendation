def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X * (A - 1) < B and X * A < Y:
        X *= A
        exp += 1
    exp += (Y - X - 1) // B
    print(exp)
