def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while True:
        if X * A >= X + B and X * A < Y:
            X *= A
            ans += 1
        elif X + B < Y:
            X += B
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()