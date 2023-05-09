def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y:
        if X * A >= X + B:
            if X * A >= Y:
                break
            X *= A
            exp += 1
        else:
            if X + B >= Y:
                break
            X += B
            exp += 1
    print(exp)
