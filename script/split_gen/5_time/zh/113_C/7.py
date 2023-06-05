def main():
    n,m = map(int,input().split())
    p_y = []
    for i in range(m):
        p_y.append(list(map(int,input().split())))
    p_y.sort(key=lambda x:x[1])
    p = 1
    x = 1
    for i in range(m):
        if p_y[i][0] == p:
            print("{0}{1}{2}".format(str(p).zfill(6),str(x).zfill(6),str(p_y[i][1]).zfill(6)))
            x+=1
        else:
            p = p_y[i][0]
            x = 1
            print("{0}{1}{2}".format(str(p).zfill(6),str(x).zfill(6),str(p_y[i][1]).zfill(6)))
            x+=1
