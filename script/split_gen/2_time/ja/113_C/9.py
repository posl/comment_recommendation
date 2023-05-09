def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    city = [0]*(n+1)
    for i in range(m):
        p = p_y[i][0]
        y = p_y[i][1]
        city[p] += 1
        print("{:06d}{:06d}".format(p,city[p]))
