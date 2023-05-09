def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(1)
        print(1, 1)
        print('U')
        return
    # まず、(0, 0)から点の距離を求める
    dist = []
    for i in range(N):
        dist.append((XY[i][0] ** 2 + XY[i][1] ** 2) ** 0.5)
    # 2番目の点までの距離が最大の点を探す
    max_dist = max(dist[1:])
    max_i = dist.index(max_dist)
    # 2番目の点までの距離が最大の点に関節を移動させる
    ans = ['U'] * (N - 1)
    ans[max_i - 1] = 'R'
    # 2番目の点までの距離が最大の点から、最大の点までの距離が最大の点に関節を移動させる
    for i in range(1, N):
        if i == max_i:
            continue
        if XY[i][0] > 0:
            ans[i - 1] = 'R'
        else:
            ans[i - 1] = 'L'
        if XY[i][1] > 0:
            ans[i - 1] += 'U'
        else:
            ans[i - 1] += 'D'
    # 最大の点の距離が1以下ならば、ループになるので不可能
    if max_dist <= 1:
        print(-1)
        return
    # 最大の点の距離が1より大きいならば、最大の点までの距離が最大の点に関節を移動させる
    ans[max_i - 1] += 'R' * int(max_dist - 1)
    # 最大の点までの距離が最大の点から、最大の点までの
