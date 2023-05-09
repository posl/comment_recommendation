def main():
    X, Y, A, B = map(int, input().split())
    count = 0
    while X * A < Y:
        if X * A - X <= B:
            count += (Y - 1 - X) // B
            break
        else:
            X *= A
            count += 1
    print(count)
