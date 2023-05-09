def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    # 1-indexed
    bit = BinaryIndexedTree(N)
    # P[i]より小さい値の個数を求める
    # P[i]より小さい値の個数がK未満ならば、P[i]はK番目に大きい値である
    ans = []
    for i in range(N):
        bit.add(P[i], 1)
        if i >= K - 1:
            if i >= K:
                bit.add(P[i - K], -1)
            left, right = 0, N
            while right - left > 1:
                mid = (left + right) // 2
                if bit.sum(mid) < K:
                    left = mid
                else:
                    right = mid
            ans.append(str(right))
    print('
'.join(ans))

if __name__ == '__main__':
    main()