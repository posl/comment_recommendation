def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    # 今いる町
    now = 0
    # 今回のテレポートで到達する町
    next = 0
    # 町の数
    town = [0]
