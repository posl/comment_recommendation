def main():
    # 读取输入
    N, M, X, T, D = map(int, input().split())
    # 计算答案
    ans = T
    for i in range(X, M):
        ans += D
    for i in range(M, N):
        ans += D
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()