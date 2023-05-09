def main():
    n,m = map(int, input().split())
    d = {}
    for i in range(m):
        p,y = map(int, input().split())
        if p not in d:
            d[p] = []
        d[p].append((i,y))
    for k in d.keys():
        d[k] = sorted(d[k], key=lambda x:x[1])
    r = [0]*m
    for k in d.keys():
        for i in range(len(d[k])):
            r[d[k][i][0]] = str(k).zfill(6) + str(i+1).zfill(6)
    for i in range(m):
        print(r[i])
