def main():
    n,x = map(int,input().split())
    v_p = [list(map(int,input().split())) for _ in range(n)]
    v_p = [[v,p] for v,p in sorted(v_p,key=lambda x:x[1],reverse=True)]
    v_p = [[v,p] for v,p in sorted(v_p,key=lambda x:x[0]*x[1],reverse=True)]
    v_p = [[v,p] for v,p in sorted(v_p,key=lambda x:x[1],reverse=True)]
    sum = 0
    for i in range(n):
        v = v_p[i][0]
        p = v_p[i][1]
        sum += v*p
        if sum > x*100:
            print(i+1)
            return
    print(-1)
