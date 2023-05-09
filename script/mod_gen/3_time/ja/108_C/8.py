def main():
    n,k=map(int,input().split())
    mod=k
    count=0
    if k%2==0:
        for i in range(k//2+1,k):
            count+=((n//k)+1)*((n//k)+1)
        count+=((n//k)+1)*((n//k)+1)*(k//2)
    else:
        for i in range(1,k):
            count+=((n//k)+1)*((n//k)+1)
    print(count)

if __name__ == '__main__':
    main()