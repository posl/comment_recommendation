def main():
    # 读入数据
    N, X = map(int, input().split())
    S = input()
    # 初始化
    score = X
    # 计算
    for i in range(N):
        if S[i] == 'o':
            score += 1
        else:
            score = max(0, score - 1)
    # 输出结果
    print(score)
