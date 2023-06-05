def main():
    #n = int(input())
    #for i in range(n):
    #    x, u = input().split()
    #    if u == "BTC":
    #        x = float(x) * 380000
    #    print(x)
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_i, u_i = input().split()
        x.append(float(x_i))
        u.append(u_i)
    sum = 0
    for i in range(n):
        if u[i] == "BTC":
            sum += x[i] * 380000
        else:
            sum += x[i]
    print(sum)

if __name__ == '__main__':
    main()