def main():
    # 三角形の辺の長さを取得
    ab, bc, ca = map(int, input().split())
    # 三角形の面積を求める
    print(int(ab * bc / 2))
