def get_input():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])
    return N, x, u
