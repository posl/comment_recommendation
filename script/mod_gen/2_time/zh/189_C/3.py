def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))
    # 计算答案
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()