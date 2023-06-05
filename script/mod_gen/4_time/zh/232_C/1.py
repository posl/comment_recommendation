def main():
    n,m=map(int,input().split())
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x,y=map(int,input().split())
        c.append(x)
        d.append(y)
    if a==c and b==d:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()