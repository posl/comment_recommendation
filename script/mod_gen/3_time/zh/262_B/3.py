def get_input():
    n,m = map(int,input().split())
    u = []
    v = []
    for i in range(m):
        u_i,v_i = map(int,input().split())
        u.append(u_i)
        v.append(v_i)
    return n,m,u,v

if __name__ == '__main__':
    get_input()