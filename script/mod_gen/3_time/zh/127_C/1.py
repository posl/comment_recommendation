def get_input():
    n,m = input().split()
    n = int(n)
    m = int(m)
    l = []
    r = []
    for i in range(m):
        l_i,r_i = input().split()
        l.append(int(l_i))
        r.append(int(r_i))
    return n,m,l,r

if __name__ == '__main__':
    get_input()