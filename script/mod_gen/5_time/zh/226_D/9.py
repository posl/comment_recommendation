def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    x.sort()
    y.sort()
    xdiff = []
    ydiff = []
    for i in range(n-1):
        xdiff.append(x[i+1]-x[i])
        ydiff.append(y[i+1]-y[i])
    xdiff.sort()
    ydiff.sort()
    print(max(xdiff[-1],ydiff[-1]))

if __name__ == '__main__':
    main()