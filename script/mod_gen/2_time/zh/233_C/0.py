def main():
    n,x = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(a[i][0]):
            if x % a[i][j + 1] == 0:
                for k in range(n):
                    if a[k][0] > 1 and a[k][1] * a[i][j + 1] == x:
                        ans += a[k][0] - 1
                    elif a[k][0] == 1 and a[k][1] == x // a[i][j + 1]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()