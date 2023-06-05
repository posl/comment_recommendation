def problems151_c():
    n,m = map(int,input().split())
    p = []
    s = []
    for i in range(m):
        p_i,s_i = input().split()
        p.append(p_i)
        s.append(s_i)
    print(p)
    print(s)

if __name__ == '__main__':
    problems151_c()