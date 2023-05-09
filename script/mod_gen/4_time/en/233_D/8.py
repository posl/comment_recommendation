def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和を求める
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    # 累積和を用いて、条件を満たす区間の数を求める
    cnt = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if S[j] - S[i] == K:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()