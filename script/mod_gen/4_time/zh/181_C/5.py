def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (x[i]-x[j])*(y[i]-y[k]) == (x[i]-x[k])*(y[i]-y[j]):
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()