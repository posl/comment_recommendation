def main():
    import math
    a,b,h,m = map(int,input().split())
    #角度の計算
    h_angle = (h*60 + m) * 0.5
    m_angle = m * 6
    #角度の差
    angle = abs(h_angle - m_angle)
    #角度をラジアンに変換
    rad = math.radians(angle)
    #三平方の定理
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(rad))
    print(c)
