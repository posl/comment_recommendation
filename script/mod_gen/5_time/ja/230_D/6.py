def main():
    n,d = map(int,input().split())
    l = []
    r = []
    for i in range(n):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    l.sort()
    r.sort()
    ans = 1
    tmp = 0
    for i in range(n):
        tmp += 1
        if i == n-1:
            break
        if l[i+1] - r[i] > d:
            ans += 1
            tmp = 0
    print(ans)

if __name__ == '__main__':
    main()