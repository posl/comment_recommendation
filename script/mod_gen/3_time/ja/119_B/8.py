def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])
    Y = 0.0
    for i in range(N):
        if u[i] == 'JPY':
            Y += x[i]
        else:
            Y += x[i] * 380000.0
    print(Y)

if __name__ == '__main__':
    main()