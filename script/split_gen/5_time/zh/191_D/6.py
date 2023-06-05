def main():
    #input
    X,Y,R = map(float,input().split())
    x = int(X*10000)
    y = int(Y*10000)
    r = int(R*10000)
    #solve
    x_min = x-r
    x_max = x+r
    y_min = y-r
    y_max = y+r
    ans = 0
    for i in range(x_min,x_max+1):
        for j in range(y_min,y_max+1):
            if (i-x)**2+(j-y)**2 <= r**2:
                ans += 1
    print(ans)
