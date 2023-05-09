def main():
    N, D = map(int, input().split())
    #壁の左端と右端の座標を格納する
    wall = []
    for i in range(N):
        L, R = map(int, input().split())
        wall.append([L, R])
    #壁の左端を昇順にソート
    wall.sort()
    #壁の右端の座標を格納する
    wall_right = []
    for i in range(N):
        wall_right.append(wall[i][1])
    #パンチを放つ回数
    punch = 0
    #パンチを放つ座標
    punch_point = 0
    #パンチを放つ座標を左端から右端へ進めていく
    for i in range(N):
        #パンチを放つ座標が、壁の左端より小さい場合
        if punch_point < wall[i][0]:
            #パンチを放つ座標を、壁の左端に合わせる
            punch_point = wall[i][0]
        #パンチを放つ座標が、壁の右端より大きい場合
        if punch_point > wall_right[i]:
            #パンチを放つ座標を、壁の右端に合わせる
            punch_point = wall_right[i]
        #パンチを放つ座標が、壁の左端と右端の間の場合
        if wall[i][0] <= punch_point <= wall_right[i]:
            #パンチを放つ回数を1回増やす
            punch += 1
            #パンチを放つ座標を、パンチを放った座標+Dにする
            punch_point += D
    print(punch)

if __name__ == '__main__':
    main()