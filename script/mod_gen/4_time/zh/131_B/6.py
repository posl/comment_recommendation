def main():
    n,l = map(int,input().split())
    print((n*l)+(n*(n-1)//2))

if __name__ == '__main__':
    main()