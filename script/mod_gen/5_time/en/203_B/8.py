def main():
    n,k = map(int,input().split())
    print((n*(n+1)*100*k//2)+(k*(k+1)*100*n//2))

if __name__ == '__main__':
    main()