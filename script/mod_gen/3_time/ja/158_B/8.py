def main():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
    elif b == 0:
        print(n)
    else:
        if a+b > n:
            print(n//a)
        else:
            print(a*(n//(a+b)) + min(a,n%(a+b)))

if __name__ == '__main__':
    main()