def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (y[i]-y[j])*(x[i]-x[k]) == (y[i]-y[k])*(x[i]-x[j]):
                    print('Yes')
                    return
    print('No')
    return

if __name__ == '__main__':
    main()