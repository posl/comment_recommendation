def main():
    # 读入数据
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # 求解
    ans = 0
    for bit in range(1 << N):
        # 选择的字符串
        T = [i for i in range(N) if bit & (1 << i)]
        # 选择的字符串的字母集合
        U = set()
        for t in T:
            U |= set(S[t])
        # 选择的字符串的字母集合的大小
        if len(U) == K:
            ans = max(ans, len(T))
    # 输出结果
    print(ans)

if __name__ == '__main__':
    main()