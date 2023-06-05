def main():
    a,b,c,d,e,f = map(int,input().split())
    A = a*b*c
    B = d*e*f
    if A > B:
        print((A-B)%998244353)
    else:
        print((B-A)%998244353)

if __name__ == '__main__':
    main()