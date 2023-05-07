def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    # 全ての要素の絶対値の和を求める
    abs_sum = sum([abs(i) for i in A])
    # すべての要素が負の場合、最大値は abs_sum となる
    if all([i < 0 for i in A]):
        print(abs_sum)
        return
    # すべての要素が正の場合、最大値は abs_sum - 2 * min(A) となる
    if all([i > 0 for i in A]):
        print(abs_sum - 2 * min(A))
        return
    # 要素に正負が混在している場合、最大値は abs_sum - 2 * min(abs(A)) となる
    print(abs_sum - 2 * min([abs(i) for i in A]))
