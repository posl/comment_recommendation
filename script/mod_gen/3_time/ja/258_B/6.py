def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, sum(a[i][j:j+n-1]) + sum(a[i][j-1:j-1-n:-1]) + sum(a[i-1][j:j-n:-1]) + sum(a[i+1][j:j+n]))
    print(ans)

if __name__ == '__main__':
    main()