def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    print("War" if x[-1] >= y[0] or x[-1] >= Y or y[0] <= X else "No War")

if __name__ == '__main__':
    main()