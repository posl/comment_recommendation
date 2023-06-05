def main():
    n,a,b = map(int,input().split())
    print(a*(n//(a+b))+min(a,n%(a+b)))

if __name__ == '__main__':
    main()