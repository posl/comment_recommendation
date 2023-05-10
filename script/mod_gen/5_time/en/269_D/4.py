def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    x_min = x[0]
    x_max = x[-1]
    y_min = y[0]
    y_max = y[-1]
    ans = 0
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            if (i+j)%2 == 0:
                continue
            else:
                if i in x and j in y:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()