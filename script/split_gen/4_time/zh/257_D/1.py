def solve():
    n = int(input())
    x = []
    y = []
    p = []
    for i in range(n):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    print(n)
