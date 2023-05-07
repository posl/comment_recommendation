def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 中央値の候補
    cand = []
    for i in range(N):
        cand.append(A[i])
        if i >= 1:
            cand.append((A[i] + A[i-1]) // 2)
    cand.append(A[-1])
    # 中央値の候補の中で、各要素が何個含まれているかを数える
    cnt = [0] * (N+1)
    for a in A:
        cnt[a] += 1
    # 中央値の候補の中で、各要素が何個含まれているかの累積和を取る
    cnt_cumsum = [0] * (N+1)
    for i in range(N):
        cnt_cumsum[i+1] = cnt_cumsum[i] + cnt[i]
    # 中央値の候補の中で、各要素が何個含まれているかの累積和の逆順の累積和を取る
    cnt_cumsum_rev = [0] * (N+1)
    for i in range(N):
        cnt_cumsum_rev[i+1] = cnt_cumsum_rev[i] + cnt[N-i-1]
    # 中央値の候補の中で、各要素が何個含まれているかの累積和の逆順の累積和の逆順を取る
    cnt_cumsum_rev_rev = [0] * (N+1)
    for i in range(N):
        cnt_cumsum_rev_rev[i+1] = cnt_cumsum_rev_rev[i] + cnt_cumsum_rev[N-i-1]
    # 中央値の候補の中で、各要素が何個含まれているかの累積和の逆順の累積和の逆順を取る
    cnt_cumsum_rev_rev_rev = [0] * (N+1

if __name__ == '__main__':
    main()