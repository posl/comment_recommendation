def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    # まず、全ての人が幸福である場合をカウントする
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            ans += 1
    # 次に、操作を行う。操作を行うと、幸福でない人が幸福になる場合がある。
    # その場合、幸福でない人の数が 2 減る。
    # また、操作を行うと、幸福でない人が幸福になる場合がある。
    # その場合、幸福でない人の数が 2 増える。
    # 以上から、操作を行うと、幸福でない人の数が 2K 減る。
    # これを考慮すると、幸福でない人の数が 2K 以下である場合の最大値を求める。
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            continue
        if i - 1 >= 0 and S[i - 1] == S[i + 1]:
            ans = max(ans, 2 * K + 1)
        else:
            ans = max(ans, 2 * K)
    # 操作を行わない場合と、操作を行う場合の最大値を比較する
    print(max(ans, N - 1))

if __name__ == '__main__':
    main()