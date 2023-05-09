def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 余りの個数をカウントするリスト
    remainder = [0] * M
    # 累積和
    cumsum = 0
    for i in range(N):
        cumsum += A[i]
        # 余りを求める
        remainder[cumsum % M] += 1
    # 組み合わせを求める
    ans = 0
    for i in range(M):
        # 余りが i であるものの組み合わせを求める
        ans += remainder[i] * (remainder[i] - 1) // 2
    print(ans)
