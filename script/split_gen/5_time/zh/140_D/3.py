def main():
    # 读入数据
    N, K = map(int, input().split())
    S = input()
    # 将字符串转换成列表
    S = list(S)
    # 计算最大快乐人数
    ans = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            ans += 1
    # 最多经过K次操作后可能出现的最大快乐人数
    ans += 2 * K
    print(min(ans, N - 1))
