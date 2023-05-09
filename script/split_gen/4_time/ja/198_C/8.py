def solve():
    # R X Y が与えられる
    R, X, Y = map(int, input().split())
    # 2点間の距離を求める
    distance = (X**2 + Y**2)**(1/2)
    # 距離がRより小さい場合
    if distance < R:
        # 原点から1歩進んだ時点で到達できる
        print(2)
    else:
        # 原点から1歩進んだ時点で到達できない
        # 原点からRずつ進んだ時点で到達できる
        print(int(distance // R) + 1)
