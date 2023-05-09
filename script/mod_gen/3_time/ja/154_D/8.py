def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    # 1からp_iまでの目が等確率で出るサイコロの期待値を求める
    E = [0.5 * (i + 1) for i in p]
    # 期待値の累積和を求める
    for i in range(N):
        if i == 0:
            continue
        E[i] += E[i - 1]
    # 期待値の最大値を求める
    ans = 0
    for i in range(N - K + 1):
        if i == 0:
            ans = E[K - 1]
        else:
            ans = max(ans, E[i + K - 1] - E[i - 1])
    print(ans)

if __name__ == '__main__':
    main()