def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while True:
        if X * A < X + B and X * A < Y:
            X *= A
            exp += 1
        else:
            exp += (Y - 1 - X) // B
            print(exp)
            return
