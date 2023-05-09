def main():
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(q):
        x,k=map(int,input().split())
        tmp=0
        for j in range(n):
            if a[j]==x:
                tmp+=1
                if tmp==k:
                    print(j+1)
                    break
        else:
            print(-1)

if __name__ == '__main__':
    main()