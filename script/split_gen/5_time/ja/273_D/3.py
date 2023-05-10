def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r = []
    c = []
    for i in range(N):
        r_i, c_i = map(int, input().split())
        r.append(r_i)
        c.append(c_i)
    Q = int(input())
    d = []
    l = []
    for i in range(Q):
        d_i, l_i = map(str, input().split())
        d.append(d_i)
        l.append(int(l_i))
    #print(H, W, r_s, c_s)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)
    # 1つ目の指示に対する処理
    #print(H, W, r_s, c_s)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)
    #print("")
    # 2つ目以降の指示に対する処理
    #print(H, W, r_s, c_s)
    #print(N)
    #print(r)
    #print(c)
    #print(Q)
    #print(d)
    #print(l)
    #print("")
