def main():
    n,a,b = map(int,input().split())
    if a%2==0 and b%2==0:
        print(0)
        return
    if a%2==0:
        a,b = b,a
    if a==1:
        print(0)
        return
    if b%a==0:
        print(0)
        return
    if n > 2*a-1:
        print((n-2*a+1)*(n-a+1)-(n-b+1)*(n-b+1))
    else:
        print(n-a+1)

if __name__ == '__main__':
    main()