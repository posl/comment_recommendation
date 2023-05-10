def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for i in range(N)]
    #print(N,K)
    #print(A)
    #print(XY)
    #中心の座標は、全員の平均値
    x_sum = 0
    y_sum = 0
    for i in range(N):
        x_sum += XY[i][0]
        y_sum += XY[i][1]
    x_center = x_sum / N
    y_center = y_sum / N
    #print(x_center,y_center)
    #中心からの距離の最大値を求める
    max_distance = 0
    for i in range(N):
        #print(XY[i][0],XY[i][1])
        distance = ((XY[i][0] - x_center) ** 2 + (XY[i][1] - y_center) ** 2) ** 0.5
        if distance > max_distance:
            max_distance = distance
    #print(max_distance)
    #明かりの強さは、中心からの距離の最大値の2乗
    result = max_distance ** 2
    print(result)
