def main():
    N = int(input())
    x0,y0 = map(int,input().split())
    x1,y1 = map(int,input().split())
    #print(N,x0,y0,x1,y1)
    #print((x1-x0)/(N/2))
    #print((y1-y0)/(N/2))
    X = x0 + (x1-x0)*(N/2-1)/(N/2)
    Y = y0 + (y1-y0)*(N/2-1)/(N/2)
    print(X,Y)

if __name__ == '__main__':
    main()