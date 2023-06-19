def main():
    a,b,c,d,e,f = map(int,input().split())
    x = a*b*c - d*e*f
    print(x%998244353)

if __name__ == '__main__':
    main()