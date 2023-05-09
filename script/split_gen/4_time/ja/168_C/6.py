def solve():
    import sys
    import math
    # 標準入力
    A,B,H,M = map(int, input().split())
    # 時針の角度
    theta_h = H * 30 + M * 0.5
    # 分針の角度
    theta_m = M * 6
    # 2本の針の角度差
    theta = abs(theta_h - theta_m)
    # 2本の針の距離
    # 余弦定理
    ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(theta)))
    # 標準出力
    print(ans)
