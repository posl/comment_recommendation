def main():
    N = int(input())
    T = input()
    #東西南北の移動をリストに
    move = []
    #東西南北の移動をリストに
    move.append([1,0])
    move.append([-1,0])
    move.append([0,-1])
    move.append([0,1])
    #向きのリストを作成
    direction = []
    #東西南北の向きをリストに
    direction.append(0)
    direction.append(1)
    direction.append(2)
    direction.append(3)
    #現在の向き
    now_direction = 0
    #現在の位置
    now_position = [0,0]
    for i in range(N):
        #Rの場合
        if T[i] == "R":
            #向きを変更
            now_direction = direction[(direction.index(now_direction) + 1) % 4]
        #Sの場合
        else:
            #移動
            now_position[0] += move[now_direction][0]
            now_position[1] += move[now_direction][1]
    print(now_position[0], now_position[1])
