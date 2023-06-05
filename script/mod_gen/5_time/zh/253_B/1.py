def main():
    # 读入数据
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    # 遍历所有的棋子，求出它们到另一个棋子的最小距离
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "o":
                continue
            # 求出到另一个棋子的最小距离
            d = 100
            for k in range(h):
                for l in range(w):
                    if s[k][l] == "o":
                        d = min(d, abs(i - k) + abs(j - l))
            # 更新答案
            ans = max(ans, d)
    # 输出答案
    print(ans)

if __name__ == '__main__':
    main()