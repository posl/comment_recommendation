def main():
    n,m = map(int,input().split())
    b = [list(map(int,input().split())) for _ in range(n)]
    a = [[(i-1)*7+j for j in range(1,8)] for i in range(1,10**100+1)]
    for i in range(10**100-n+1):
        for j in range(7-m+1):
            if a[i][j:j+m] == b[0] and a[i+1][j:j+m] == b[1]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()