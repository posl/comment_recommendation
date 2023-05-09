def main():
    import math
    a,b,h,m = map(int,input().split())
    #時針の回転角度
    theta_h = h * 30 + m * 0.5
    #分針の回転角度
    theta_m = m * 6
    #時針と分針の角度の差
    theta = abs(theta_h - theta_m)
    if theta > 180:
        theta = 360 - theta
    ans = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))
    print(ans)
