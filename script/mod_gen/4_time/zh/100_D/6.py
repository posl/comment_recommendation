def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = 0
    for i in range(8):
        b = []
        for j in range(n):
            tmp = 0
            for k in range(3):
                if ((i>>k)&1):
                    tmp += a[j][k]
                else:
                    tmp -= a[j][k]
            b.append(tmp)
        b.sort(reverse=True)
        tmp = 0
        for j in range(m):
            tmp += b[j]
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()