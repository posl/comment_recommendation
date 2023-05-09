def main():
    #入力
    N, R = map(int, input().split())
    #出力
    print(R + 100 * (10 - N) if N < 10 else R)
