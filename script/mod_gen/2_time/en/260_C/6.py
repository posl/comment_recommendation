def main():
    N, X, Y = map(int, input().split())
    if N == 1:
        print(0)
        return
    else:
        print(X + Y + (N-2)*(X+Y))

if __name__ == '__main__':
    main()