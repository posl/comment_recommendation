def main():
    n,m = map(int,input().split())
    data = []
    for i in range(m):
        p,y = map(int,input().split())
        data.append([p,y,i])
    data.sort(key=lambda x:x[1])
    ans = []
    cnt = [0]*n
    for i in range(m):
        p,y,i = data[i]
        cnt[p-1] += 1
        ans.append([i,cnt[p-1]])
    ans.sort(key=lambda x:x[0])
    for i in range(m):
        p,x = ans[i]
        print(str(p+1).zfill(6)+str(x).zfill(6))

if __name__ == '__main__':
    main()