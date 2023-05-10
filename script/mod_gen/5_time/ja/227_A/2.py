def main():
    n,k,a = map(int,input().split())
    print((k-1+n-a)%n+1)

if __name__ == '__main__':
    main()