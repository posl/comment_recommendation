def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x0,y0 = map(int,input().split())
        x.append(x0)
        y.append(y0)
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            ans += ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
    print(ans*2/N)
