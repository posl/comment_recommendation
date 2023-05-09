def main():
    n,m = map(int,input().split())
    city = []
    for i in range(m):
        p,y = map(int,input().split())
        city.append([p,y,i])
    city = sorted(city,key=lambda x:(x[0],x[1]))
    ans = []
    for i in range(m):
        p,y,i = city[i]
        ans.append([i,(str(p).zfill(6)+str(i+1).zfill(6))])
    ans = sorted(ans,key=lambda x:x[0])
    for i in range(m):
        print(ans[i][1])
