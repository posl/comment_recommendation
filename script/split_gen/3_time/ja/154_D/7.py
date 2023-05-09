def main():
    import sys
    readline = sys.stdin.readline
    import numpy as np
    N, K = map(int, readline().split())
    p = np.array(list(map(int, readline().split())))
    # 累積和
    s = np.cumsum(p)
    # 合計
    s = s[K:] - s[:-K]
    # 期待値
    e = (s + K) / 2
    print(np.max(e))
