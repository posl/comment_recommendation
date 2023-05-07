def main():
    # 入力
    r, D, x = map(int, input().split())
    # 出力
    for i in range(10):
        x = r * x - D
        print(x)
