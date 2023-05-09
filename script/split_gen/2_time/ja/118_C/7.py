def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 最小値を求める問題なので、最大公約数を求める
    from fractions import gcd
    from functools import reduce
    print(reduce(gcd, A))
