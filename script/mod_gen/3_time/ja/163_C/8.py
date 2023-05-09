def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 部下の数をカウントする配列
    # 0番目は使わない
    cnt = [0] * (N + 1)
    # 部下の数をカウント
    for i in range(N - 1):
        cnt[A[i]] += 1
    # 部下の数を出力
    for i in range(1, N + 1):
        print(cnt[i])

if __name__ == '__main__':
    main()