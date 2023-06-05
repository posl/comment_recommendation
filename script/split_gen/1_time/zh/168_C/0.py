def problem168_c():
    # 读入数据
    a, b, h, m = map(int, input().split())
    # 时针和分针的角度
    theta_h = h * 30 + m / 2
    theta_m = m * 6
    # 时针和分针的坐标
    x_h = a * math.cos(math.radians(theta_h))
    y_h = a * math.sin(math.radians(theta_h))
    x_m = b * math.cos(math.radians(theta_m))
    y_m = b * math.sin(math.radians(theta_m))
    # 时针和分针的距离
    ans = math.sqrt((x_h - x_m) ** 2 + (y_h - y_m) ** 2)
    print(ans)
