def main():
    #入力
    N, D = map(int, input().split())
    #出力
    print((N + D * 2) // (D * 2 + 1))
