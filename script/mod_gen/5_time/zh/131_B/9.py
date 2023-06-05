def main():
    n,l = map(int,input().split())
    if n==2:
        print(l+1)
    elif l>=0:
        print(sum(range(l+1,l+n)))
    elif l+n-1<0:
        print(sum(range(l+n-1,l-1,-1)))
    else:
        print(sum(range(l,l+n-1)))

if __name__ == '__main__':
    main()