def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j]):
                    print('Yes')
                    return
    print('No')
    return

if __name__ == '__main__':
    main()