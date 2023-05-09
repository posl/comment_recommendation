def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    #print(points)
    #x, yの座標をそれぞれソート
    x_points = sorted(points, key=lambda x: x[0])
    y_points = sorted(points, key=lambda x: x[1])
    #print(x_points)
    #print(y_points)
    #x, yの座標のリストを作る
    x_list = []
    y_list = []
    for i in range(N):
        x_list.append(x_points[i][0])
        y_list.append(y_points[i][1])
    #print(x_list)
    #print(y_list)
    #x, yの座標のリストから、重複を削除したリストを作る
    x_list2 = list(set(x_list))
    y_list2 = list(set(y_list))
    #print(x_list2)
    #print(y_list2)
    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y_len)
    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y_len)
    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y_len)
    #x, yの座標のリストから、重複を削除したリストの長さを取得
    x_len = len(x_list2)
    y_len = len(y_list2)
    #print(x_len)
    #print(y
