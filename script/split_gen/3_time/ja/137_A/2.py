def main():
    # 標準入力受け取り
    a, b = map(int, input().split())
    # 計算
    print(max(a+b, a-b, a*b))
