def main():
    import sys
    import math
    from collections import deque
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import dijkstra, shortest_path
    def input(): return sys.stdin.readline().rstrip()
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x, y, r = [], [], []
    for i in range(N):
        x_, y_, r_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        r.append(r_)
    # 点sから点tへの最短距離を求める
    # 点sから点tへの最短距離が、点sから点tへの最短経路のうちの最長辺の長さ以下ならば、Yes
    # 点sから点tへの最短距離が、点sから点tへの最短経路のうちの最長辺の長さより大きければ、No
    # 点sから点tへの最短距離を求める
    # 点sから点tへの最短経路のうちの最長辺の長さを求める
    # 点sから点tへの最短経路のうちの最長辺の長さが、点sから点tへの最短距離以下ならば、Yes
    # 点sから点tへの最短経路のうちの最長辺の長さが、点sから点tへの最短距離より大きければ、No
    # 点sから点tへの最短経路のうちの最長辺の長さを求める
    # 点sから点tへの最短距離を求

if __name__ == '__main__':
    main()