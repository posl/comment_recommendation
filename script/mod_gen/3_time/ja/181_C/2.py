def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                    print("Yes")
                    exit()
    print("No")

if __name__ == '__main__':
    main()