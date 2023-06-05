def main():
    # 读取输入
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # 答案
    ans = 0
    # 遍历N个字符串
    for i in range(N):
        # 遍历M个字符串
        for j in range(M):
            # 如果S[i]的最后三个字符与T[j]的最后三个字符一致
            if S[i][-3:] == T[j]:
                # 答案加1
                ans += 1
                # 跳出循环
                break
    # 输出答案
    print(ans)
