def main():
    #入力
    n,d = map(int,input().split())
    #壁の情報を受け取る
    wall = []
    for i in range(n):
        wall.append(list(map(int,input().split())))
    #壁の左端を昇順にソート
    wall.sort(key=lambda x:x[0])
    #壁の右端を昇順にソート
    wall.sort(key=lambda x:x[1])
    #右端が最も小さい壁を取得
    min_wall = wall[0]
    #右端が最も小さい壁の右端
    min_wall_right = min_wall[1]
    #右端が最も小さい壁の左端
    min_wall_left = min_wall[0]
    #右端が最も小さい壁の左端からdだけ離れた位置
    min_wall_left_d = min_wall_left + d
    #左端が最も小さい壁の右端よりdだけ離れた位置
    min_wall_right_d = min_wall_right + d
    #右端が最も小さい壁の左端からdだけ離れた位置が右端が最も小さい壁の右端よりdだけ離れた位置よりも小さい場合、
    #右端が最も小さい壁の左端からdだけ離れた位置が右端が最も小さい壁の右端よりdだけ離れた位置よりも大きい場合、
    #右端が最も小さい壁の左端からdだけ離れた位置が右端が最も小さい壁の右端よりdだけ離れた位置と等しい場合、
    #パンチを1回放つことですべての壁を破壊することができる
    if min_wall_left_d < min_wall_right_d or min_wall_left_d > min_wall_right_d or min_wall_left_d == min_wall_right_d:
        print(1)
    #右端が最も小さい壁の
