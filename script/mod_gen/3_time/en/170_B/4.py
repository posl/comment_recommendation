def main():
    X, Y = map(int, input().split())
    if X == 1 and Y == 2:
        print("Yes")
        return
    for i in range(1, X):
        if i * 2 + (X - i) * 4 == Y:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()