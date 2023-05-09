def main():
    X, Y, A, B = map(int, input().split())
    ans = 0
    while X * A < Y:
        if X * A - X <= B:
            ans += 1
            X *= A
        else:
            break
    ans += (Y - X - 1) // B
    print(ans)

if __name__ == '__main__':
    main()