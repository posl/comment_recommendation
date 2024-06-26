def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # 1, 2, 4, 8, 9, 10, 11, ... という数列のうち、aに含まれないものを求める
    # 1, 2, 4, 8, 9, 10, 11, ... のうち、aに含まれるものを除けばよい
    # 1, 2, 4, 8, 9, 10, 11, ... は、2進数で考えると、
    # 001, 010, 100, 1000, 1001, 1010, 1011, ... となる
    # 2進数の各桁を見ていくと、aの各桁よりも小さい数であれば、その桁は0である
    # 例えば、a = 10, 11, 12, 13, 14 のとき、
    # 2進数で考えると、
    # 1010, 1011, 1100, 1101, 1110
    # となる
    # このとき、2進数の各桁を見ていくと、
    # 1桁目は、aの1桁目よりも小さい数であれば0である
    # 2桁目は、aの2桁目よりも小さい数であれば0である
    # 3桁目は、aの3桁目よりも小さい数であれば0である
    # 4桁目は、aの4桁目よりも小さい数であれば0である
    # となる
    # つまり、2進数の各桁を見ていくと、aの各桁よりも小さい
