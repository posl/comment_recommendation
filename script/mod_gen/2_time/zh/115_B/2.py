def main():
    # 读取输入
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    # 计算
    p.sort()
    p[-1] = p[-1] // 2
    print(sum(p))

if __name__ == '__main__':
    main()