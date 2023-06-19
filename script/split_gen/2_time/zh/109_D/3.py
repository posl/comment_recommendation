def solve():
    H,W = map(int,input().split())
    a = []
    for i in range(H):
        a.append(list(map(int,input().split())))
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j < W - 1:
                    a[i][j+1] += 1
                    ans.append([i+1,j+1,i+1,j+2])
                elif i < H - 1:
                    a[i+1][j] += 1
                    ans.append([i+1,j+1,i+2,j+1])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])
solve()
