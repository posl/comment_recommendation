def sol():
    n,m = map(int,input().split())
    s = []
    c = []
    for i in range(m):
        s_i,c_i = map(int,input().split())
        s.append(s_i)
        c.append(c_i)
    for i in range(10**(n-1),10**n):
        flag = True
        for j in range(m):
            if int(str(i)[s[j]-1]) != c[j]:
                flag = False
                break
        if flag:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    sol()