def main():
    # 读入
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # 处理
    a_min = max(a)
    b_min = min(b)
    # 输出
    if a_min > b_min:
        print(0)
    else:
        print(b_min - a_min + 1)

if __name__ == '__main__':
    main()