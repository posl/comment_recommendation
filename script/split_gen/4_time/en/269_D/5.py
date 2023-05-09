def main():
    #input
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi,yi = map(int,input().split())
        x.append(xi)
        y.append(yi)
    #solve
    ans = 0
    for i in range(n):
        if (x[i]-1,y[i]-1) in zip(x,y) or (x[i]-1,y[i]) in zip(x,y) or (x[i],y[i]-1) in zip(x,y) or (x[i],y[i]+1) in zip(x,y) or (x[i]+1,y[i]) in zip(x,y) or (x[i]+1,y[i]+1) in zip(x,y):
            ans += 1
    #output
    print(n-ans)
