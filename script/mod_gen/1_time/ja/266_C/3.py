def main():
    # 入力
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    # 処理
    # 三角形の面積を求める
    s1 = (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2
    s2 = (ax * (cy - dy) + cx * (dy - ay) + dx * (ay - cy)) / 2
    s3 = (ax * (dy - by) + dx * (by - ay) + bx * (ay - dy)) / 2
    s4 = (bx * (dy - cy) + dx * (cy - by) + cx * (by - dy)) / 2
    s = abs(s1 + s2 + s3 + s4)
    # 出力
    if s == 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()