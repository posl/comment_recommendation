def main():
    #入力
    N, D = map(int, input().split())
    #監視員を配置
    print((N + D * 2) // (D * 2 + 1))
