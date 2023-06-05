def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    # print(p_y)
    ans = [0]*m
    cnt = [0]*n
    for i in range(m):
        cnt[p_y[i][0]-1] += 1
        ans[i] = str(p_y[i][0]).zfill(6) + str(cnt[p_y[i][0]-1]).zfill(6)
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()