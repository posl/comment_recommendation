def main():
    n,a,b = map(int,input().split())
    s = input()
    if n%2==0:
        if a<b:
            print(a*n)
        else:
            print(b*n)
    else:
        if a<b:
            print(a*(n-1)+b)
        else:
            print(b*(n-1)+a)

if __name__ == '__main__':
    main()