def main():
    n, m = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int, input().split()))[0])
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** n):
        tmp = []
        for j in range(n):
            if ((i >> j) & 1) == 1:
                tmp.append(1)
            else:
                tmp.append(0)
        flag = True
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                if tmp[s[j][l] - 1] == 1:
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = False
        if flag == True:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()