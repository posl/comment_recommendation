def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 人iが隣り合う人のリスト
    neighbor = [[] for _ in range(N+1)]
    for a, b in AB:
        neighbor[a].append(b)
        neighbor[b].append(a)
    # 人iが隣り合う人の数
    neighbor_cnt = [len(neighbor[i]) for i in range(1, N+1)]
    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt2 = [neighbor[i].count(i) for i in range(1, N+1)]
    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt3 = [neighbor[i].count(i) for i in range(1, N+1)]
    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt4 = [neighbor[i].count(i) for i in range(1, N+1)]
    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt5 = [neighbor[i].count(i) for i in range(1, N+1)]
    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt6 = [neighbor[i].count(i) for i in range(1, N+1)]
    # 人iが隣り合う人のうち、隣り合う人のリストに自分自身が含まれているか
    neighbor_cnt7 = [neighbor[i].count(i
