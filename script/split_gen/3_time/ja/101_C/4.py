def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    # 連続したK個の要素を選ぶときに、選んだ要素の中の最小値で置き換える
    # 連続したK個の要素を選ぶときの総数はN-K+1通り
    # 連続したK個の要素の中の最小値は、K個の要素の中の最小値の中の最小値
    # すなわち、K個の要素の中の最小値を求める
    # K個の要素の中の最小値を求めるには、K個の要素を選ぶときの総数回の操作が必要
    # したがって、K個の要素を選ぶときの総数回の操作が必要
    print(N-K+1)
