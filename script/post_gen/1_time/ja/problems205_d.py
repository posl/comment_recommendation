Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ...
    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ...
    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ...
    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ...
    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ...

    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ...
    # 1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, ...
    # 1, 2, 4, 8, 9, 10,

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]

    for i in k:
        print(a[i-1])

=======
Suggestion 4

def main():
    #入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #問題文の通り、A_1, A_2, ..., A_N のいずれとも異なる正整数のうち、小さい方から数えて K_i 番目のものを求める
    #10**18 までで、2**60 までの整数は表せる
    #2**60 までの整数を、A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #2**60 までの整数を、A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #A_1, A_2, ..., A_N のいずれとも異なる正整数として、小さい順に並べる
    #A_1, A_2, ..., A_N のいずれとも異な

=======
Suggestion 5

def main():
    # 入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    # 1, 2, 4, 8, 9, 10, 11, ... という数列を作る
    B = [1]
    for i in range(1, N+Q):
        B.append(B[i-1]+A[i-1])
    # クエリ処理
    for k in K:
        # 二分探索
        ok = 0
        ng = N+Q
        while ng-ok > 1:
            mid = (ok+ng)//2
            if B[mid] >= k:
                ng = mid
            else:
                ok = mid
        # 出力
        print(A[ok]-B[ok]+k)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #print("N, Q = ", N, Q)
    #print("A = ", A)
    #print("K = ", K)

    # Aの中の最大値を求める
    max_a = max(A)
    #print("max_a = ", max_a)

    # Aの中の最大値より大きい数を求める
    # 数が多いときは、素数を使う
    # 2, 3, 5, 7, 11, ...
    # 2, 3, 5, 7, 11, 13, 17, ...
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, ...
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, ...
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, ...
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, ...
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ...

    # 素数のリストを作る
    # 2, 3, 5, 7, 11, ...
    # 2, 3, 5, 7,

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    A.sort()
    A.append(10**18)
    ans = []
    for k in K:
        if k <= A[0]:
            ans.append(k)
            continue
        left = 0
        right = N
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] - A[mid-1] - 1 < k:
                k -= A[mid] - A[mid-1] - 1
                left = mid
            else:
                right = mid
        ans.append(A[left] + k)
    for a in ans:
        print(a)

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # aの最大値を求める
    a_max = max(a)
    # aの最大値を超える最小の2のべき乗
    a_max_p2 = 1
    while a_max_p2 <= a_max:
        a_max_p2 *= 2
    # aの最大値を超える最小の2のべき乗の配列を作成
    a_max_p2_list = [1]
    while a_max_p2_list[-1] <= a_max:
        a_max_p2_list.append(a_max_p2_list[-1] * 2)
    # aの最大値を超える最小の2のべき乗の配列を逆順に並べる
    a_max_p2_list.reverse()
    # aの最大値を超える最小の2のべき乗の配列の要素数
    a_max_p2_list_len = len(a_max_p2_list)
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリスト
    over_a_max_p2_list = []
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリストの要素数
    over_a_max_p2_list_len = 0
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリストの要素数を求める
    for i in range(a_max_p2_list_len):
        if a_max_p2_list[i] > n:
            over_a_max_p2_list_len = i
            break
    # aの最大値を超える最小の2のべき乗の配列の要素数を超える数値のリ

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]

    # 1を除く、aの要素を2乗したものをリストに格納
    b = [i**2 for i in a if i != 1]
    # aの要素を2乗したものの最大値を求める
    max_b = max(b)
    # aの要素の最大値を求める
    max_a = max(a)
    # 1を除く、aの要素を2乗したものの最大値を求める
    max_b = max(b)

    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものをリストに格納
    c = [i for i in b if i < max_a]
    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値を求める
    max_c = max(c)

    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1を除く、aの要素を2乗したものをリストに格納
    d = [i for i in c if i < max_b]
    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1を除く、aの要素を2乗したものの最大値を求める
    max_d = max(d)

    # aの要素の最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1を除く、aの要素を2乗したものの最大値より小さい、1
