def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = [a[i] for i in range(0,n,2)]
    c = [a[i]-1 for i in range(1,n,2)]
    d = b+c
    if sum(d)<=x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()