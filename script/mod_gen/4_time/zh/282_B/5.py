def main():
    n, m = map(int, input().split())
    a = [[0]*m for i in range(n)]
    for i in range(n):
        a[i] = list(input())
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if a[i][k] == 'o' or a[j][k] == 'o':
                    continue
                else:
                    flag = False
            if flag:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()