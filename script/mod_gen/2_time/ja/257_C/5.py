def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # 体重の昇順に並び替え
    W_sort = sorted(W)
    # 体重の昇順に並び替えたときのインデックス
    W_sort_index = sorted(range(N), key=lambda x: W[x])
    # 体重の昇順に並び替えたときのインデックスの逆順
    W_sort_index_reverse = sorted(range(N), key=lambda x: W[x], reverse=True)
    # 体重の昇順に並び替えたときの、体重が i 以上の人数
    W_sort_cnt = [0] * (N + 1)
    for i in range(N):
        W_sort_cnt[i + 1] = W_sort_cnt[i] + (S[W_sort_index[i]] == '1')
    # 体重の降順に並び替えたときの、体重が i 未満の人数
    W_sort_reverse_cnt = [0] * (N + 1)
    for i in range(N):
        W_sort_reverse_cnt[i + 1] = W_sort_reverse_cnt[i] + (S[W_sort_index_reverse[i]] == '0')
    ans = 0
    for i in range(N):
        ans = max(ans, W_sort_cnt[i] + W_sort_reverse_cnt[N - i])
    print(ans)

if __name__ == '__main__':
    main()