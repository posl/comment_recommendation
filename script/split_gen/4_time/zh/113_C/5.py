def main():
    n,m = map(int,input().split())
    city = []
    for i in range(m):
        p,y = map(int,input().split())
        city.append([p,y,i])
    city.sort(key=lambda x:x[1])
    ans = []
    for i in range(m):
        p,y,idx = city[i]
        ans.append([p,str(i+1).zfill(6),idx])
    ans.sort(key=lambda x:x[2])
    for i in range(m):
        print(ans[i][0]+ans[i][1])
