def main():
    # (x1, y1), (x2, y2), (x3, y3), (x4, y4) = [list(map(int, input().split())) for _ in range(4)]
    # (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1) は、
    # (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1) が正ならば、
    # 3 点 (x1, y1), (x2, y2), (x3, y3) は反時計回りに並んでいる
    # が、
    # 3 点 (x1, y1), (x2, y2), (x3, y3) は反時計回りに並んでいるときには、
    # (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1) は正になる
    # ということらしい
    # つまり、(x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1) が正ならば、
    # 3 点 (x1, y1), (x2, y2), (x3, y3) は反時計回りに並んでいる
    # が、
    # 3 点 (x1, y1), (x2, y2), (x3, y3) は反時計回りに並んでいるときには、
    # (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1) は正になる
    # ということらしい
    # つまり、(x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 -

if __name__ == '__main__':
    main()