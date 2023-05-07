def main():
    #入力
    N, K, A = map(int, input().split())
    #出力
    print((A + K - 2) % N + 1)
