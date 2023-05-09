def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # 1. 1つ目の駅を決める
    # 2. 2つ目の駅を決める
    # 3. 1つ目の駅と2つ目の駅の距離を計算する
    # 4. 1つ目の駅のコストに2つ目の駅のコストと距離を足したものを計算する
    # 5. 1～4の中で最小のものを出力する
    # 1. 1つ目の駅を決める
    # 1つ目の駅のコストの最小値を求める
    # 1つ目の駅のコストの最小値の座標を求める
    min_cost = float('inf')
    min_cost_coordinate = [0, 0]
    for i in range(H):
        for j in range(W):
            if min_cost > A[i][j]:
                min_cost = A[i][j]
                min_cost_coordinate = [i, j]
    # 2. 2つ目の駅を決める
    # 2つ目の駅のコストの最小値を求める
    # 2つ目の駅のコストの最小値の座標を求める
    min_cost_2 = float('inf')
    min_cost_coordinate_2 = [0, 0]
    for i in range(H):
        for j in range(W):
            if min_cost_2 > A[i][j] and min_cost_coordinate != [i, j]:
                min_cost_2 = A[i][j]
                min_cost_coordinate_2 = [i, j]
    # 3. 1つ目の駅と2つ目の駅の距離を計算する
    distance = abs(min_cost_coordinate[0] - min_cost_coordinate_

if __name__ == '__main__':
    main()