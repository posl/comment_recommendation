def get_input():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    return n, x, u
