def main():
    # 標準入力から整数を受け取る
    N = int(input())
    # 標準入力から整数のリストを受け取る
    H = list(map(int, input().split()))
    # 最も高い橋の高さを求める
    H_max = max(H)
    # 最も高い橋の何番目にあるかを求める
    H_max_idx = H.index(H_max) + 1
    # 結果を出力する
    print(H_max_idx)

if __name__ == '__main__':
    main()