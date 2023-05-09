def main():
    #入力
    N, R = map(int, input().split())
    #出力
    if N < 10:
        print(R + (100 * (10 - N)))
    else:
        print(R)
