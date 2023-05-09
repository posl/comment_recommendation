def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            tmp = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**(1/2)
            if max < tmp:
                max = tmp
    print(max)

if __name__ == '__main__':
    main()