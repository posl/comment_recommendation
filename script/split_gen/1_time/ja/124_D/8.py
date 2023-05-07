def main():
    N, K = map(int, input().split())
    S = input()
    # 0, 1 それぞれの区間の長さのリストを作る
    # 例: S = 00010 のとき
    # 0 の区間: [3, 1]
    # 1 の区間: [1]
    intervals = []
    current = S[0]
    count = 0
    for s in S:
        if s == current:
            count += 1
        else:
            intervals.append(count)
            count = 1
            current = s
    intervals.append(count)
    # 0, 1 それぞれの区間の長さのリストから、
    # 0 の区間の長さのリストを作る
    # 例: S = 00010 のとき
    # 0 の区間: [3, 1]
    intervals_0 = []
    for i in range(0, len(intervals), 2):
        intervals_0.append(intervals[i])
    # 0 の区間の長さのリストから、
    # 0 の区間の長さのリストのうち、
    # K 個を選んで足した値の最大値を求める
    # 例: K = 1 のとき
    # 0 の区間: [3, 1]
    # 0 の区間の長さのリストのうち、1 個を選んで足した値の最大値: 3 + 1 = 4
    # 例: K = 2 のとき
    # 0 の区間: [3, 1]
    # 0 の区間の長さのリストのうち、2 個を選んで足した値の最大値: 3 + 1 = 4
    ans = 0
    for i in range(min(K, len(intervals_0))):
        ans += intervals_0[i]
    for i in range(min(K, len(intervals_0)) - 1,
