def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    # 三角形の底辺の長さ
    a = ((x1 - x0)**2 + (y1 - y0)**2)**(1/2)
    # 三角形の高さ
    h = a * (3**(1/2)) / 2
    # 三角形の底辺から頂点までの距離
    b = a / 2
    # 三角形の底辺の中点
    x2 = (x0 + x1) / 2
    y2 = (y0 + y1) / 2
    # 三角形の底辺の中点から頂点までの距離
    c = h / 2
    # 三角形の底辺の中点と頂点の角度
    angle = math.atan2(y1 - y0, x1 - x0)
    # 三角形の底辺の中点から頂点までの距離と角度から頂点の座標を求める
    x3 = x2 + b * math.cos(angle + math.pi / 6)
    y3 = y2 + b * math.sin(angle + math.pi / 6)
    print(x3, y3)
