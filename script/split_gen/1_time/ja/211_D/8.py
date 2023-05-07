def main():
    #N: 都市数, M: 道路数
    N, M = map(int, input().split())
    #都市1から各都市への道路の数
    road = [0] * (N + 1)
    #都市1から各都市への道路数をカウント
    for i in range(M):
        A, B = map(int, input().split())
        road[A] += 1
        road[B] += 1
    #都市1から各都市への道路数が0のものは都市1から都市Nへ移動できないので0を出力
    if road[1] == 0 or road[N] == 0:
        print(0)
    else:
        #都市1から都市Nへの道路数を出力
        print(road[1] * road[N])
