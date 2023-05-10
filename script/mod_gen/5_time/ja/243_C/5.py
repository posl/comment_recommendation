def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    s = input()
    # 右向きの人と左向きの人を分けて考える
    # 同じ向きの人同士は衝突しないので、
    # 右向きの人の中でy座標が一番小さい人と
    # 左向きの人の中でy座標が一番大きい人が衝突する
    # また、右向きの人の中でy座標が一番大きい人と
    # 左向きの人の中でy座標が一番小さい人が衝突する
    # 右向きの人の中でy座標が一番小さい人
    right_min = 10**9
    right_min_index = 0
    for i in range(n):
        if s[i] == "R":
            if xy[i][1] < right_min:
                right_min = xy[i][1]
                right_min_index = i
    # 左向きの人の中でy座標が一番大きい人
    left_max = 0
    left_max_index = 0
    for i in range(n):
        if s[i] == "L":
            if xy[i][1] > left_max:
                left_max = xy[i][1]
                left_max_index = i
    # 右向きの人の中でy座標が一番大きい人
    right_max = 0
    right_max_index = 0
    for i in range(n):
        if s[i] == "R":
            if xy[i][1] > right_max:
                right_max = xy[i][1]
                right_max_index = i
    # 左向きの人の中でy座標が一番小さい人
    left_min = 10**9
    left_min_index = 0
    for i in range(n):
        if s[i] == "L":
            if

if __name__ == '__main__':
    main()