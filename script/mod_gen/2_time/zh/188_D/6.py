def main():
    s = input().split()
    N = int(s[0])
    C = int(s[1])
    a = []
    b = []
    c = []
    for i in range(N):
        s = input().split()
        a.append(int(s[0]))
        b.append(int(s[1]))
        c.append(int(s[2]))
    d = []
    for i in range(N):
        d.append((a[i],c[i]))
        d.append((b[i]+1,-c[i]))
    d.sort(key=lambda x:x[0])
    ans = 0
    t = 0
    x = 0
    for i in range(2*N):
        if d[i][0] != x:
            ans += min(C,t)*(d[i][0]-x)
            x = d[i][0]
        t += d[i][1]
    print(ans)

if __name__ == '__main__':
    main()