def main():
    # 入力
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    # 処理
    A = [i for i in A if i != X]
    # 出力
    print(*A)
