def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                xi = x[i]
                yi = y[i]
                xj = x[j]
                yj = y[j]
                xk = x[k]
                yk = y[k]
                if (xi-xj)*(yi-yk) == (xi-xk)*(yi-yj):
                    continue
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()