def main():
    # input
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # compute
    x_max = max(x)
    y_min = min(y)
    # output
    if x_max < y_min and X < y_min and y_min <= Y:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()