def main():
    n = int(input())
    x = []
    y = []
    for i in range(0,n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(0,n):
        for j in range(i,n):
            ans = max(ans,((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5)
    print(ans)

if __name__ == '__main__':
    main()