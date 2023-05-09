def main():
    n = int(input())
    a = [list(map(int,input().split())) for i in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = a[i][j] ^ a[j][i]
    ans = 0
    for i in range(1,1<<n):
        b = 0
        for j in range(n):
            if (i>>j)&1:
                b = b ^ a[j][j]
        ans = max(ans,b)
    print(ans)

if __name__ == '__main__':
    main()