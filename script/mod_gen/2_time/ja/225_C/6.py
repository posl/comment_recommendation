def main():
    n,m = map(int,input().split())
    b = [list(map(int,input().split())) for _ in range(n)]
    a = [[(i-1)*7+j for j in range(1,8)] for i in range(1,10**4+1)]
    for i in range(10**4-n+1):
        for j in range(7-m+1):
            if b == [a[i+k][j:j+m] for k in range(n)]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()