def main():
    # 標準入力の受け取り
    h, w = map(int, input().split())
    h2, w2 = map(int, input().split())
    print(h * w - (h2 * w + w2 * h - h2 * w2))
