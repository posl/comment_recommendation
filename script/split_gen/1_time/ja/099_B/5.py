def main():
    a, b = map(int, input().split())
    # どの塔の高さが大きいかを判定する
    if a > b:
        a, b = b, a
    # 2 つの塔の高さを求める
    a_height = (a + 1) * a // 2
    b_height = (b + 1) * b // 2
    # 2 つの塔の高さの差を求める
    height = b_height - a_height
    # 2 つの塔の高さの差を出力する
    print(height)
