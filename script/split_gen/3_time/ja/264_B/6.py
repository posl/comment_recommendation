def main():
    # R C
    # 1 ≦ R, C ≦ 15
    # R, C は整数
    R, C = map(int, input().split())
    # 黒白を判定
    if (R % 2 == 0 and C % 2 == 0) or (R % 2 == 1 and C % 2 == 1):
        print("black")
    else:
        print("white")
