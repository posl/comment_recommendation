def get_input():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        for j in range(a[i]):
            x_tmp, y_tmp = map(int, input().split())
            x.append(x_tmp)
            y.append(y_tmp)
    return n, a, x, y
