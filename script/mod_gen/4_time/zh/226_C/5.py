def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        t1, k1, *a1 = map(int, input().split())
        t.append(t1)
        k.append(k1)
        a.append(a1)
    #print(t)
    #print(k)
    #print(a)
    ans = 0
    for i in range(n):
        if k[i] == 0:
            ans += t[i]
        else:
            tmax = 0
            for j in range(k[i]):
                if tmax < t[a[i][j]-1]:
                    tmax = t[a[i][j]-1]
            t[i] += tmax
            ans += t[i]
    print(ans)

if __name__ == '__main__':
    main()