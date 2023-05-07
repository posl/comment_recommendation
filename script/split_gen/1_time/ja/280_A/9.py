def main():
    # H,W
    H, W = map(int, input().split())
    # S_i
    S = [input() for _ in range(H)]
    # 出力
    print(sum([s.count('#') for s in S]))
