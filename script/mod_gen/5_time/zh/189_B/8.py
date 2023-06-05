def main():
    n,x=map(int,input().split())
    v=[0]*n
    p=[0]*n
    for i in range(n):
        v[i],p[i]=map(int,input().split())
    s=0
    for i in range(n):
        s+=v[i]*p[i]
        if s>x*100:
            print(i+1)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()