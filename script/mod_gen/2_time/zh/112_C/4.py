def main():
    # 读取输入
    n, t = map(int, input().split())
    # 读取输入
    lines = []
    for i in range(n):
        c, t = map(int, input().split())
        lines.append((c, t))
    # 找出花费不超过时间T的路线的最小成本
    lines = sorted(lines, key=lambda x: x[0])
    for line in lines:
        if line[1] <= t:
            print(line[0])
            break
    else:
        print('TLE')

if __name__ == '__main__':
    main()