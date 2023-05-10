def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(H * W - sum(s.count('#') for s in S))
