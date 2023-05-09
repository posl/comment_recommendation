def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(m)]
    c = [list(map(int, input().split())) for i in range(m)]
    for i in range(m):
        a[i][0] -= 1
        c[i][0] -= 1
    ans = "No"
    for i in range(2**n):
        p = []
        for j in range(n):
            if (i >> j) & 1:
                p.append(j)
        if len(p) != n/2:
            continue
        flag = True
        for j in range(m):
            if (a[j][0] in p) ^ (a[j][1] in p):
                flag = False
            if (c[j][0] in p) ^ (c[j][1] in p):
                flag = False
        if flag:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()