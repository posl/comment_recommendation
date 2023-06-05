def main():
    n,m = map(int,input().split())
    x,y,z = [],[],[]
    for i in range(n):
        x_i,y_i,z_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
        z.append(z_i)
    x.sort(reverse=True)
    y.sort(reverse=True)
    z.sort(reverse=True)
    ans = 0
    for i in range(2**3):
        sign = [1]*3
        for j in range(3):
            if (i>>j)&1:
                sign[j] = -1
        x_sum,y_sum,z_sum = 0,0,0
        for j in range(m):
            x_sum += x[j]*sign[0]
            y_sum += y[j]*sign[1]
            z_sum += z[j]*sign[2]
        ans = max(ans,abs(x_sum)+abs(y_sum)+abs(z_sum))
    print(ans)

if __name__ == '__main__':
    main()