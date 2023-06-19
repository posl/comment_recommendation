def solve(H, W, r_s, c_s, N, r, c, Q, d, l):
    # x, y = r_s, c_s
    # for i in range(Q):
    #     if d[i] == "L":
    #         for j in range(l[i]):
    #             y -= 1
    #             if (x, y) in zip(r, c):
    #                 y += 1
    #     elif d[i] == "R":
    #         for j in range(l[i]):
    #             y += 1
    #             if (x, y) in zip(r, c):
    #                 y -= 1
    #     elif d[i] == "U":
    #         for j in range(l[i]):
    #             x -= 1
    #             if (x, y) in zip(r, c):
    #                 x += 1
    #     else:
    #         for j in range(l[i]):
    #             x += 1
    #             if (x, y) in zip(r, c):
    #                 x -= 1
    #     print(x, y)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 0:上, 1:下, 2:左, 3:右
    d_idx = ["U", "D", "L", "R"]
    # 0:左, 1:右, 2:上, 3:下
    d_idx_rev = ["L", "R", "U", "D"]
    r = [x - 1 for x in r]
    c = [x - 1 for x in c]
    # 与当前方块相邻的方块
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(4):
            if 0 <= r[i] + dx[j] < H and 0 <= c[i] + dy[j] < W:
                adj[i].append((r[i] + dx[j], c[i] + dy[j]))
    # print(adj)
    # 当前方块的左右上下是否有墙
    wall =
