def main():
    X, Y, A, B = map(int, input().split())
    cnt = 0
    while X * A < X + B and X * A < Y:
        X *= A
        cnt += 1
    cnt += (Y - X - 1) // B
    print(cnt)
main()
