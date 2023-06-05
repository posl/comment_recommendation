def main():
    # 读入数据
    N = int(input())
    A = [int(i) for i in input().split()]
    # 累积和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 累积最大值
    M = [0] * (N + 1)
    for i in range(N):
        M[i + 1] = max(M[i], S[i + 1])
    # 答案
    ans = float('inf')
    for i in range(1, N - 1):
        # M[i] - S[i] : B + C
        # M[N] - M[i] : D + E
        ans = min(ans, max(M[i] - S[i], M[N] - M[i]))
    # 输出
    print(ans)
