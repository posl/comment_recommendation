def main():
    n,m = map(int,input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        a = list(map(int,input().split()))
        k.append(a[0])
        s.append(a[1:])
    p = list(map(int,input().split()))
    #print(k,s,p)
    ans = 0
    for i in range(2**n):
        #print(i)
        flag = 0
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                #print(l,s[j][l])
                if (i>>(s[j][l]-1))&1:
                    cnt += 1
            if cnt%2 != p[j]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()