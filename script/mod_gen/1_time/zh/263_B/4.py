def main():
    # 读取输入
    N = int(input())
    P = list(map(int, input().split()))
    # 从第i个人开始，向上追溯到第1个人，计算代数
    ans = 0
    for i in range(N):
        p = i + 1
        while p != -1:
            ans += 1
            p = P[p - 1]
            # print(p)
        # print('---')
    print(ans)

if __name__ == '__main__':
    main()