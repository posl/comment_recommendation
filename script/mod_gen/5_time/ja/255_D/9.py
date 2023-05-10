def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # print(A)
    # print(X)
    # Aの最大値を求める
    maxA = max(A)
    # Aの最大値を2進数で表したときの桁数を求める
    maxA_bin = bin(maxA)
    maxA_bin_len = len(maxA_bin) - 2
    # print(maxA)
    # print(maxA_bin)
    # print(maxA_bin_len)
    # Aの全ての要素を2進数で表したときの桁数を求める
    A_bin = [bin(a) for a in A]
    A_bin_len = [len(a) - 2 for a in A_bin]
    # print(A_bin)
    # print(A_bin_len)
    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)
    # print(maxA_bin_len)
    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)
    # print(maxA_bin_len)
    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)
    # print(maxA_bin_len)
    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)
    # print(maxA_bin_len)
    # Aの全ての要素を2進数で表したときの桁数の最大値を求める
    maxA_bin_len = max(A_bin_len)
    # print(maxA_bin_len)
    # Aの全ての要素を2進数で表したときの桁数の最大値

if __name__ == '__main__':
    solve()