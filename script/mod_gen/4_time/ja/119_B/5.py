def main():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    y = 0
    for i in range(n):
        if u[i] == 'BTC':
            y += x[i] * 380000.0
        else:
            y += x[i]
    print(y)

if __name__ == '__main__':
    main()