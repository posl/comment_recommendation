def main():
    n,m = map(int, input().split())
    data = []
    for i in range(m):
        p,y = map(int, input().split())
        data.append([p,y,i])
    data.sort(key=lambda x:x[1])
    ans = [0] * m
    cnt = [0] * (n+1)
    for i in range(m):
        p,y,idx = data[i]
        cnt[p] += 1
        ans[idx] = str(p).zfill(6) + str(cnt[p]).zfill(6)
    for i in range(m):
        print(ans[i])

if __name__ == '__main__':
    main()