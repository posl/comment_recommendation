def main():
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j] < d:
                count += 1
    print(count)

if __name__ == '__main__':
    main()