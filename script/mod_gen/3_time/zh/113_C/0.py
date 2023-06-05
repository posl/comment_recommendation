def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for i in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y2 = [p_y[i]+[i] for i in range(m)]
    p_y2.sort(key=lambda x:x[2])
    ans = []
    for i in range(m):
        ans.append([p_y2[i][0],p_y2[i][2]+1])
    ans.sort(key=lambda x:x[1])
    for i in range(m):
        print(str(ans[i][0]).zfill(6)+str(ans[i][1]).zfill(6))

if __name__ == '__main__':
    main()