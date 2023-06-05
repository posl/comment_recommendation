def main():
    # 读入数据
    n, m = map(int, input().split())
    a = [input() for _ in range(2*n)]
    # 生成初始排名
    rank = [[i+1, 0] for i in range(2*n)]
    # 比赛
    for i in range(m):
        # 每一轮比赛
        for j in range(n):
            # 每一场比赛
            p1, p2 = rank[2*j][0]-1, rank[2*j+1][0]-1
            if (a[p1][i] == 'G' and a[p2][i] == 'C') or \
                    (a[p1][i] == 'C' and a[p2][i] == 'P') or \
                    (a[p1][i] == 'P' and a[p2][i] == 'G'):
                rank[2*j][1] -= 1
            elif (a[p1][i] == 'G' and a[p2][i] == 'P') or \
                    (a[p1][i] == 'C' and a[p2][i] == 'G') or \
                    (a[p1][i] == 'P' and a[p2][i] == 'C'):
                rank[2*j+1][1] -= 1
        rank.sort(key=lambda x: (x[1], x[0]))
    # 输出结果
    for i in range(2*n):
        print(rank[i][0])

if __name__ == '__main__':
    main()