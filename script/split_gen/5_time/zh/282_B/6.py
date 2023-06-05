def main():
    # 读取输入
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    # 答案
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if all(S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)):
                ans += 1
    print(ans)
