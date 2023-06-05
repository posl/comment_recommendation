def solve():
    # 读入数据
    N, D = map(int, input().split())
    L = []
    R = []
    for i in range(N):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    # 求出所有墙的左右端点
    L_all = []
    R_all = []
    for i in range(N):
        L_all.append(L[i])
        R_all.append(R[i])
        L_all.append(L[i] - D)
        R_all.append(R[i] - D)
    L_all.sort()
    R_all.sort()
    # 从最左端开始，依次求出各个墙的所需打孔次数
    ans = 0
    l = 0
    r = 0
    for i in range(len(L_all)):
        while r < len(R_all) and R_all[r] <= L_all[i]:
            r += 1
        ans = max(ans, r - l)
        if L_all[i] == R_all[l]:
            l += 1
    print(ans)
solve()
