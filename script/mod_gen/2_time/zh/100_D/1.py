def get_max_value():
    n, m = map(int, input().split(" "))
    x = []
    y = []
    z = []
    for i in range(n):
        x_i, y_i, z_i = map(int, input().split(" "))
        x.append(x_i)
        y.append(y_i)
        z.append(z_i)
    value = []
    for i in range(n):
        value.append(x[i] + y[i] + z[i])
    value.sort(reverse=True)
    ans = 0
    for i in range(m):
        ans += value[i]
    print(ans)
get_max_value()
