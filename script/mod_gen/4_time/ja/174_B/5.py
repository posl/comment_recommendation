def main():
    n,d = map(int,input().split())
    x = []
    y = []
    for i in range(n):
        xi,yi = map(int,input().split())
        x.append(xi)
        y.append(yi)
    count = 0
    for i in range(n):
        if x[i]**2 + y[i]**2 <= d**2:
            count += 1
    print(count)

if __name__ == '__main__':
    main()