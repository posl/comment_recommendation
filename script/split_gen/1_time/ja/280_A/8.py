def main():
    #入力
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #出力
    print(S.count('#'))
