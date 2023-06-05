def main():
    # 读取数据
    N = int(input())
    X = [0]*N
    Y = [0]*N
    H = [0]*N
    for i in range(N):
        X[i], Y[i], H[i] = map(int, input().split())
    # 从高度最大的点开始，逐个遍历所有点
    for i in range(N):
        if H[i] > 0:
            cx, cy, ch = X[i], Y[i], H[i]
            break
    # 逐个遍历所有点
    for x in range(101):
        for y in range(101):
            # 当前点的高度
            h = ch + abs(x - cx) + abs(y - cy)
            # 判断当前点是否满足条件
            for i in range(N):
                if H[i] != max(h - abs(x - X[i]) - abs(y - Y[i]), 0):
                    break
            else:
                print(x, y, h)
                return

if __name__ == '__main__':
    main()