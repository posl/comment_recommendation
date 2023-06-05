def main():
    h, w, r_s, c_s = map(int, input().split())
    n = int(input())
    r = [0] * n
    c = [0] * n
    for i in range(n):
        r[i], c[i] = map(int, input().split())
    q = int(input())
    d = [0] * q
    l = [0] * q
    for i in range(q):
        d[i], l[i] = input().split()
        l[i] = int(l[i])
    # 墙的位置
    wall = [[0] * w for i in range(h)]
    for i in range(n):
        wall[r[i] - 1][c[i] - 1] = 1
    # 高桥的位置
    r_s -= 1
    c_s -= 1
    # 移动方向
    dr = [-1, 0, 1, 0] # 上、右、下、左
    dc = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    # 移动
    for i in range(q):
        for j in range(4):
            if d[i] == dir[j]:
                for k in range(l[i]):
                    # 如果下一个位置没有墙，就移动过去
                    if 0 <= r_s + dr[j] < h and 0 <= c_s + dc[j] < w and wall[r_s + dr[j]][c_s + dc[j]] == 0:
                        r_s += dr[j]
                        c_s += dc[j]
                    # 如果下一个位置有墙，就不移动
                    else:
                        break
                break
        print(r_s + 1, c_s + 1)

if __name__ == '__main__':
    main()