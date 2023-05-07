def main():
    # 入力
    A, B, C = map(int, input().split())
    # 出力
    print("Yes" if A**2 + B**2 < C**2 else "No")
