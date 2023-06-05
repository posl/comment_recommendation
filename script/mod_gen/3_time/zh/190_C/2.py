def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a.append(int(input().split()[0]))
        b.append(int(input().split()[1]))
    k = int(input())
    c = []
    d = []
    for i in range(k):
        c.append(int(input().split()[0]))
        d.append(int(input().split()[1]))
    ans = 0
    for i in range(2**k):
        dish = [0 for i in range(n)]
        for j in range(k):
            if ((i >> j) & 1):
                dish[c[j]-1] += 1
            else:
                dish[d[j]-1] += 1
        cnt = 0
        for j in range(m):
            if dish[a[j]-1] >= 1 and dish[b[j]-1] >= 1:
                cnt += 1
        ans = max(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()