def main():
    n,m = map(int,input().split())
    k = []
    s = []
    for i in range(m):
        a = list(map(int,input().split()))
        k.append(a[0])
        s.append(a[1:])
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                if i&(2**(s[j][l]-1)):
                    cnt += 1
            if cnt%2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()