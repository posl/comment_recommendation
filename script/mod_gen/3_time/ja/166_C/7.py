def main():
    # 1行目
    N, M = map(int, input().split())
    # 2行目
    H = list(map(int, input().split()))
    # 3行目以降
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 1. 道を繋ぐ2点の標高を比較
    # 2. 標高が同じなら、道を消す
    # 3. 標高が異なるなら、高い方の標高を保存
    # 4. 高い方の標高を保存した展望台は、良い展望台とする
    # 道を繋ぐ2点の標高を比較
    for i in range(M):
        # 標高が同じなら、道を消す
        if H[AB[i][0]-1] == H[AB[i][1]-1]:
            H[AB[i][0]-1] = 0
            H[AB[i][1]-1] = 0
        # 標高が異なるなら、高い方の標高を保存
        else:
            # 高い方の標高を保存した展望台は、良い展望台とする
            if H[AB[i][0]-1] < H[AB[i][1]-1]:
                H[AB[i][0]-1] = 0
            else:
                H[AB[i][1]-1] = 0
    # 良い展望台の数を出力
    print(sum(1 for i in H if i != 0))

if __name__ == '__main__':
    main()