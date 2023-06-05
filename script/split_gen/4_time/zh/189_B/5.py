def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        v_,p_ = map(int,input().split())
        v.append(v_)
        p.append(p_)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]
        if sum > x*100:
            print(i+1)
            exit()
    print(-1)
