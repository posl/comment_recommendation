def main():
    h,w,r_s,c_s = map(int,input().split())
    n = int(input())
    r_c = []
    for i in range(n):
        r_c.append(list(map(int,input().split())))
    q = int(input())
    d_l = []
    for i in range(q):
        d_l.append(list(input().split()))
    print(h,w,r_s,c_s)
    print(n)
    print(r_c)
    print(q)
    print(d_l)
    return
