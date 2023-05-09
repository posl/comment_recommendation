def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    # ここに処理を書く
    print(max(S) if len(S) > 0 else -1)
