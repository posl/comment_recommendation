def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()