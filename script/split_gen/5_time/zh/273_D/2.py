def main():
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    rcs = [list(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    ds = [list(input().split()) for _ in range(Q)]
    # print(H, W, rs, cs)
    # print(N)
    # print(rcs)
    # print(Q)
    # print(ds)
    # # 初始化地图
    # map = [['.' for _ in range(W)] for _ in range(H)]
    # for rc in rcs:
    #     map[rc[0] - 1][rc[1] - 1] = '#'
    # map[rs - 1][cs - 1] = 'T'
    # for m in map:
    #     print(m)
    # # 指令
    # for d in ds:
    #     if d[0] == 'L':
    #         for _ in range(int(d[1])):
    #             if map[rs - 1][cs - 2] == '#':
    #                 pass
    #             else:
    #                 cs -= 1
    #             map[rs - 1][cs - 1] = 'T'
    #     elif d[0] == 'R':
    #         for _ in range(int(d[1])):
    #             if map[rs - 1][cs] == '#':
    #                 pass
    #             else:
    #                 cs += 1
    #             map[rs - 1][cs - 1] = 'T'
    #     elif d[0] == 'U':
    #         for _ in range(int(d[1])):
    #             if map[rs - 2][cs - 1] == '#':
    #                 pass
    #             else:
    #                 rs -= 1
    #             map[rs - 1][cs - 1] = 'T'
    #     elif d[0] == 'D':
    #         for _ in range(int(d[1])):
    #             if map[rs][cs - 1] == '#':
    #                 pass
    #             else:
    #                 rs += 1
    #             map[
