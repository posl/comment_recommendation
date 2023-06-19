def main():
    # 读取输入
    n = int(input())
    x = [0] * n
    y = [0] * n
    h = [0] * n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    # 暴力枚举
    for cx in range(101):
        for cy in range(101):
            # 计算最小高度
            H = -1
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            # 验证其他高度是否一致
            for i in range(n):
                tmp = max(H - abs(x[i] - cx) - abs(y[i] - cy), 0)
                if h[i] != tmp:
                    H = -1
                    break
            if H >= 0:
                print(cx, cy, H)
                return

if __name__ == '__main__':
    main()