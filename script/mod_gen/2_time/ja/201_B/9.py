def main():
    # 入力
    N = int(input())
    S_T = [input().split() for _ in range(N)]
    # 高さを整数に変換
    S_T = [[S, int(T)] for S, T in S_T]
    # 高さを基準にソート
    S_T.sort(key=lambda x: x[1], reverse=True)
    # 出力
    print(S_T[1][0])

if __name__ == '__main__':
    main()