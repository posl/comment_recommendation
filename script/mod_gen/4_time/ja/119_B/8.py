def main():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        x_u = input().split()
        x.append(float(x_u[0]))
        u.append(x_u[1])
    y = 0
    for i in range(n):
        if u[i] == "JPY":
            y += x[i]
        else:
            y += x[i] * 380000.0
    print(y)
main()

if __name__ == '__main__':
    main()