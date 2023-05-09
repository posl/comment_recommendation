def main():
    # 入力
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    dx, dy = map(int, input().split())
    # 処理
    # 四角形の4つの内角が全て180度未満であることを確認する
    # 4つの内角が全て180度未満である場合はYes、そうでない場合はNoを出力する
    A = (ax - cx) * (by - cy) - (ay - cy) * (bx - cx)
    B = (bx - dx) * (cy - dy) - (by - dy) * (cx - dx)
    C = (cx - ax) * (dy - ay) - (cy - ay) * (dx - ax)
    D = (dx - bx) * (ay - by) - (dy - by) * (ax - bx)
    # 出力
    if A > 0 and B > 0 and C > 0 and D > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()