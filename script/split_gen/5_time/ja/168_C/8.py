def solve():
    # 時針と分針の長さがそれぞれ A センチメートル、B センチメートルであるアナログ時計
    A, B = map(int, input().split())
    # 時針と分針それぞれの片方の端点は同じ定点に固定されており、この点を中心としてそれぞれの針は一定の角速度で時計回りに回転します。
    # 時針は 12 時間で、分針は 1 時間で 1 周します。
    # 0 時ちょうどに時針と分針は重なっていました。
    # ちょうど H 時 M 分になったとき、2 本の針の固定されていない方の端点は何センチメートル離れているでしょうか。
    H, M = map(int, input().split())
    # 2 本の針は図のようになり、答えは 5 センチメートルです。
    # 2 本の針は常に一定の角速度で回ることに注意してください。
    # 時針の長さが A であるとき、時針の角速度は 2π/(12×60) です。
    # 分針の長さが B であるとき、分針の角速度は 2π/60 です。
    # 時針と分針が H 時 M 分になっているとき、時針と分針の角度の差は、時針の角速度と分針の角速度の差に等しいです。
    # つまり、時針と分針の角度の差は 11M/2 です。
    # これをラジアンに変換すると、11π