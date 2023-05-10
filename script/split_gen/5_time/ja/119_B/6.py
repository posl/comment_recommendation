def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    total = 0
    for i in range(N):
        if u[i] == "BTC":
            total += x[i] * 380000.0
        else:
            total += x[i]
    print(total)
