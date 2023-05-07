def main():
    #input
    A,B,H,M = map(int,input().split())
    #calculate
    #各針の角度を求める
    hour_angle = 30*H + 0.5*M
    minute_angle = 6*M
    #各針の角度の差を求める
    angle = abs(hour_angle - minute_angle)
    #各針の角度の差をラジアンに変換する
    angle = math.radians(angle)
    #各針の長さの二乗を足し合わせる
    C = A**2 + B**2 - 2*A*B*math.cos(angle)
    #output
    print(math.sqrt(C))
