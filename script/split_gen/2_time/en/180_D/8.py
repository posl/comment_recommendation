def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while True:
        if X * A < Y and X * A - X <= B:
            X *= A
            exp += 1
        else:
            break
    exp += (Y - X - 1) // B
    print(exp)
