def main():
    N = int(input())
    x = []
    u = []
    for i in range(N):
        x1,u1 = input().split()
        x.append(float(x1))
        u.append(u1)
    sum = 0
    for i in range(N):
        if u[i] == 'JPY':
            sum += x[i]
        elif u[i] == 'BTC':
            sum += x[i] * 380000.0
    print(sum)

if __name__ == '__main__':
    main()