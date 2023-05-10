def check(X,Y):
    # 鶴の数をt, 亀の数をkとすると
    # t + k = X
    # 2 * t + 4 * k = Y
    # これを解くと
    # t = Y / 2 - X
    # k = 2 * X - Y / 2
    # である。
    # これが整数であることを確認すればよい。
    t = Y / 2 - X
    k = 2 * X - Y / 2
    if t >= 0 and k >= 0 and t == int(t) and k == int(k):
        return True
    else:
        return False
