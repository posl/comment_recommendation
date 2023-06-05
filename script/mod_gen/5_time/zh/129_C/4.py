def main():
    n,m = map(int,input().split())
    a=[]
    for i in range(m):
        a.append(int(input()))
    a.sort()
    a.append(n)
    b=[0]*(n+1)
    b[0]=1
    for i in range(1,n+1):
        if i in a:
            continue
        elif i-1 in a and i-2 in a:
            b[i]=0
        elif i-1 in a:
            b[i]=b[i-2]
        elif i-2 in a:
            b[i]=b[i-1]
        else:
            b[i]=b[i-1]+b[i-2]
    print(b[n]%1000000007)

if __name__ == '__main__':
    main()