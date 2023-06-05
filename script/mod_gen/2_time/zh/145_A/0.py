def solve(a,b,x):
    if x <= a*a*b/2:
        # 这种情况下，水的高度小于等于a/2，所以倾斜角度为45°
        return 45
    else:
        # 这种情况下，水的高度大于a/2，所以倾斜角度为
        # tanθ = (a^2*b-x)/(a^3/2)
        # θ = atan((a^2*b-x)/(a^3/2))
        return math.atan((a*a*b-x)/(a*a*a/2))*180/math.pi

if __name__ == '__main__':
    solve()