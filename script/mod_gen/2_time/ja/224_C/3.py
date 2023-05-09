def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (x[j]-x[i])*(y[k]-y[i])-(x[k]-x[i])*(y[j]-y[i]) != 0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()