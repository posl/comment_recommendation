def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(m)]
    c = [list(map(int,input().split())) for i in range(m)]
    for i in range(m):
        a[i][0] -= 1
        a[i][1] -= 1
        c[i][0] -= 1
        c[i][1] -= 1
    b = [i for i in range(n)]
    ans = "No"
    for i in range(2**n):
        d = [0]*n
        for j in range(n):
            if ((i >> j) & 1):
                d[j] = 1
        for j in range(m):
            if d[a[j][0]] != d[a[j][1]]:
                break
        else:
            for j in range(m):
                if d[c[j][0]] != d[c[j][1]]:
                    break
            else:
                ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()