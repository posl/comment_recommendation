def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    # シミュレーション
    # 1回の操作で、連続するK個の要素の最小値を求める
    # これを全ての要素が同じ値になるまで繰り返す
    # ただし、連続するK個の要素の最小値がK個以上ある場合は、
    # 最小値のうちK個を選んで、それ以外を最小値にする
    # この操作は、最小値のうちK個を選んで、それ以外を最小値にする
    # という操作を繰り返すことと等しい
    # 操作回数を数える
    cnt = 0
    while True:
        # 最小値の個数をカウント
        min_cnt = 0
        for i in range(1, N+1):
            if A[i] == min(A):
                min_cnt += 1
        if min_cnt == N:
            break
        # 最小値の個数がK個以上ある場合
        if min_cnt >= K:
            # 最小値のうちK個を選んで、それ以外を最小値にする
            for i in range(1, N+1):
                if A[i] == min(A):
                    A[i] = min(A)
                else:
                    A[i] = min(A)+1
            cnt += 1
        # 最小値の個数がK個未満の場合
        else:
            # 最小値のうちK個を選んで、それ以外を最小値にする
            for i in range(1, N+1):
                if A[i] == min(A):
                    A[i] = min(A)
                else:
                    A[i] = min(A)+1

if __name__ == '__main__':
    main()