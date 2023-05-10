def main():
    n, m, x, y = map(int, input().split())
    x_max = max(list(map(int, input().split())))
    y_min = min(list(map(int, input().split())))
    if x_max < y_min and x < y_min and y_min <= y:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()