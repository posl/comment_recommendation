def main():
    N,M,T=map(int,input().split())
    a=[0]*M
    b=[0]*M
    for i in range(M):
        a[i],b[i]=map(int,input().split())
    now=N
    for i in range(M):
        now=now-(a[i]-b[i-1])
        if now<=0:
            print("No")
            return
        now=now+(b[i]-a[i])
        if now>N:
            now=N
    now=now-(T-b[M-1])
    if now<=0:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()