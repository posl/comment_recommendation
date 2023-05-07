def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))
main()  # 出力結果: 実行時間制限超過
