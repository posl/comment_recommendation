def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y:
        if X*A < X+B:
            X *= A
            exp += 1
        else:
            X += B
            exp += 1
    print(exp-1)
