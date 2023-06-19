def main():
    #读入数据
    n,x = map(int,input().split())
    v = []
    p = []
    for _ in range(n):
        v_i,p_i = map(int,input().split())
        v.append(v_i)
        p.append(p_i)
    #计算酒精含量
    alcohol = 0
    for i in range(n):
        alcohol += v[i]*p[i]
        if alcohol > x*100:
            print(i+1)
            return
    print(-1)
