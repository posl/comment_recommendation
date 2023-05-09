def main():
    n,x,y = map(int,input().split())
    u = [0]*(n-1)
    v = [0]*(n-1)
    for i in range(n-1):
        u[i],v[i] = map(int,input().split())
    for i in range(n-1):
        if u[i] == x and v[i] == y:
            print(i+1)
        elif u[i] == y and v[i] == x:
            print(i+1)
        else:
            pass

if __name__ == '__main__':
    main()