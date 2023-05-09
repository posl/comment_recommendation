def main():
    n,m = map(int,input().split())
    for i in range(1,m-n+2):
        print(i,end=' ')
        for j in range(1,n):
            print(i+j,end=' ')
        print()

if __name__ == '__main__':
    main()