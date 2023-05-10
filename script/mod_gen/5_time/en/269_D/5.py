def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        tmp_x, tmp_y = map(int, input().split())
        x.append(tmp_x)
        y.append(tmp_y)
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    #print(x_min, x_max, y_min, y_max)
    cnt = 0
    for i in range(n):
        if x_min <= x[i] <= x_max and y_min <= y[i] <= y_max:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()