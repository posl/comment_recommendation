def main():
    # 读取输入
    p, q, r = map(int, input().split())
    # 计算最短时间
    print(min(p + q, q + r, r + p))

if __name__ == '__main__':
    main()