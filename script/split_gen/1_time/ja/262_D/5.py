def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # 2^N-1 通りの選び方
    # 2^N-1 通りの選び方のうち、整数の平均値を持つものが何通りかを求める
    # 2^N-1 通りの選び方は、選ばない場合と選ぶ場合の2通り
    # 選ばない場合は、選ぶ場合の数に含まれているので、
    # 選ぶ場合の数を求める
    # 選ぶ場合の数は、2^(N-1) 通り
    # 2^(N-1) 通りの選び方のうち、整数の平均値を持つものが何通りかを求める
    # 2^(N-1) 通りの選び方は、選ばない場合と選ぶ場合の2通り
    # 選ばない場合は、選ぶ場合の数に含まれているので、
    # 選ぶ場合の数を求める
    # 選ぶ場合の数は、2^(N-2) 通り
    # 2^(N-2) 通りの選び方のうち、整数の平均値を持つものが何通りかを求める
    # 2^(N-2) 通りの選び方は、選ばない場合と選ぶ場合の2通り
    # 選ばない場合は、選ぶ場合の数に含まれているので、
    # 選ぶ場合の数を求める
    # 選ぶ場合の数は、2^(N-3