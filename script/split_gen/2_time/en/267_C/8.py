def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 1-indexed
    A = [0] + A
    # A[i] - A[i-1] の値を格納
    # [0, A[1] - A[0], A[2] - A[1], ..., A[N] - A[N-1]]
    # これを累積和し、M個ずつの累積和の最大値を求める
    diff = [0] * (N + 1)
    for i in range(1, N + 1):
        diff[i] = A[i] - A[i - 1]
    # print(diff)
    # 累積和
    for i in range(1, N + 1):
        diff[i] += diff[i - 1]
    # print(diff)
    # M個ずつの累積和の最大値を求める
    ans = 0
    for i in range(M, N + 1):
        ans = max(ans, diff[i] - diff[i - M])
    print(ans)
