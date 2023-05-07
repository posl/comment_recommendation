def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 最大値を求める
    max_a = max(A)
    for i in range(N):
        print(S[N] - S[i] - A[i] + max_a)

if __name__ == '__main__':
    main()