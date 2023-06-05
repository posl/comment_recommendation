def main():
    # 读入数据
    A, B, N = map(int, input().split())
    # 计算结果
    ans = int(A * min(B - 1, N) / B)
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()