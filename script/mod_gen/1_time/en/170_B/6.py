def main():
    X, Y = map(int, input().split())
    if X == Y == 1:
        print("Yes")
        return
    for i in range(X + 1):
        if 2 * i + 4 * (X - i) == Y:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()