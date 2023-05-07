def main():
    n,k,m=map(int,input().split())
    a=list(map(int,input().split()))
    if sum(a)+m*n>=n*m:
        print(max(0,n*m-sum(a)))
    else:
        print(-1)
main()

if __name__ == '__main__':
    main()