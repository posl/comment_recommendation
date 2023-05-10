def main():
    n,m = map(int,input().split())
    for i in range(n,m+1):
        for j in range(i+1,m+1):
            print(i,j)

if __name__ == '__main__':
    main()