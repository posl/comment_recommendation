def main():
    a,b,c,d,e,f = map(int,input().split())
    print((a*b*c-d*e*f)%998244353)
main()

if __name__ == '__main__':
    main()