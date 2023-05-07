def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # 1, 2, 4, 8, 9, 10, 11, ... のように、異なる正整数を小さい順に並べると、
    # 1, 2, 4, 8, 9, 10, 11, ... となる。
    # これを A の要素と合わせて、小さい順に並べると、
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... となる
    # つまり、A の要素を i とすると、
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... の i 番目の要素は、
    # A の要素の i 番目の要素を 2 進数で表したときの 1 の個数と一致する
    # 例えば、A = (3, 5, 6, 7) のとき、
    # 3 = 11 なので 1 の個数は 2 個
    # 5 = 101 なので 1 の個数は 2 個
    # 6 = 110 なので 1 の個数は 2 個
    # 7 = 111 なので 1 の個数は 3 個
    # となるので、
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... は
    # 1, 2, 2, 3, 2, 2, 3, 4, 2, 2, 3, ...
