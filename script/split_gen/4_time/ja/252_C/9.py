def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # print(N, S)
    # S[0]を基準にして、S[0]とS[i]の差分を求める
    # 1 と 2 の差分を求める
    # 2 と 3 の差分を求める
    # 3 と 4 の差分を求める
    # ...
    # N-1 と N の差分を求める
    # 1 と N の差分を求める
    # 2 と N の差分を求める
    # 3 と N の差分を求める
    # ...
    # N-2 と N の差分を求める
    # N-1 と N の差分を求める
    # その中で最小の値を求める
    # 0 と 1 の差分を求める
    # 1 と 2 の差分を求める
    # 2 と 3 の差分を求める
    # 3 と 4 の差分を求める
    # ...
    # N-2 と N-1 の差分を求める
    # N-1 と N の差分を求める
    # その中で最小の値を求める
    # 0 と 2 の差分を求める
    # 1 と 3 の差分を求める
    # 2 と 4 の差分を求める
    # 3 と 5 の差分を求める
    # ...
    # N-1 と N の差分を求める
    # その中で最小の値を求める
    # 0 と 3 の差分を求める
    # 1 と 4 の差分を求める
    # 2 と 5 の