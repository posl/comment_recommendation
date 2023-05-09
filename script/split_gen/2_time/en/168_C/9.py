def main():
    a,b,h,m = map(int,input().split())
    #print(a,b,h,m)
    #1時間を何分にするか
    h_m = 60
    #1時間を何度にするか
    h_d = 360
    #1分を何度にするか
    m_d = 6
    #時針の角度
    h_d += h_d/h_m*m
    #分針の角度
    m_d += m_d*m
    #print(h_d,m_d)
    #時針と分針の角度差
    d = abs(h_d-m_d)
    #print(d)
    #角度をラジアンに変換
    d_rad = d/360*2*math.pi
    #print(d_rad)
    #三角関数を使って答えを求める
    c = math.sqrt(a**2+b**2-2*a*b*math.cos(d_rad))
    print(c)
