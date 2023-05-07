def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i] + A[i])
    # 累積和の差分を求める
    diff = []
    for i in range(N - M + 1):
        diff.append(sumA[i + M] - sumA[i])
    # 累積和の差分の最大値を求める
    ans = 0
    for i in range(N - M + 1):
        ans = max(ans, diff[i] + i * M)
    print(ans)

if __name__ == '__main__':
    main()