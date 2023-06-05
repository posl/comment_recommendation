def main():
    # 读取输入
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    # 计算
    ans = (h - r + 1) * (w - c + 1)
    # 输出
    print(ans)

if __name__ == '__main__':
    main()