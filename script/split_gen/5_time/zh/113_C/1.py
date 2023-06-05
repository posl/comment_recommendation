def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for i in range(m)]
    p_y.sort(key=lambda x:x[1])
    p = 0
    x = 1
    ans = [0]*m
    for i in range(m):
        if p_y[i][0] != p:
            p = p_y[i][0]
            x = 1
        ans[i] = [p_y[i][0],x]
        x += 1
    ans.sort(key=lambda x:x[0])
    for i in range(m):
        print(str(ans[i][0]).zfill(6)+str(ans[i][1]).zfill(6))
