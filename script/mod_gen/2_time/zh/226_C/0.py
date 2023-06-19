def main():
    n = int(input())
    t = []
    k = []
    a = []
    for i in range(n):
        a.append([])
        t1, k1, *a1 = map(int, input().split())
        t.append(t1)
        k.append(k1)
        for j in range(k1):
            a[i].append(a1[j])
    print(a)
    print(t)
    print(k)
    ans = 0
    for i in range(n):
        if k[i] == 0:
            ans = max(ans, t[i])
        else:
            ans = max(ans, t[i]+t[a[i][0]-1])
    print(ans)

if __name__ == '__main__':
    main()