def main():
    # 读取输入
    A, B, C, D, E, F = map(int, input().split())
    # 计算答案
    ans = (A * B * C - D * E * F) % 998244353
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()