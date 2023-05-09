def main():
    n,m=map(int,input().split())
    a=[1]*n
    while True:
        print(*a)
        if a[-1]==m:
            for i in range(n-1,-1,-1):
                if a[i]!=m:
                    a[i]+=1
                    for j in range(i+1,n):
                        a[j]=a[i]
                    break
            else:
                break
        else:
            a[-1]+=1

if __name__ == '__main__':
    main()