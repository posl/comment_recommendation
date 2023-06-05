def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    # 生成结果
    ans = []
    for i in range(2 ** N):
        ans.append(0)
    for i in range(N):
        ans[2 * i] = 1
    for i in range(N):
        ans[A[i] - 1] = ans[i] + 1
    # 输出结果
    for i in range(2 ** N):
        print(ans[i])

if __name__ == '__main__':
    main()