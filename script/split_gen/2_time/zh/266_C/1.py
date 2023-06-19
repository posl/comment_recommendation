def is_convex(a, b, c, d):
    # 逆时针排列
    if a[0] * b[1] + b[0] * c[1] + c[0] * d[1] + d[0] * a[1] - a[1] * b[0] - b[1] * c[0] - c[1] * d[0] - d[1] * a[0] > 0:
        return True
    else:
        return False
