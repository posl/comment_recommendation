def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x_max = max(x)
    y_min = min(y)
    if x_max < y_min and x_max < Y and X < y_min:
        print("No War")
    else:
        print("War")
main()

if __name__ == '__main__':
    main()