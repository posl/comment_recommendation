def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j]*b[j]
        if tmp + c > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()