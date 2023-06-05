def main():
    n, m = map(int, input().split())
    u = []
    v = []
    for i in range(m):
        u_, v_ = map(int, input().split())
        u.append(u_)
        v.append(v_)
    print(n, m)
    print(u)
    print(v)
