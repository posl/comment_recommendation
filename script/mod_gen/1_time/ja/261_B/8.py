def main():
    # 入力
    N = int(input())
    A = [input() for _ in range(N)]
    # 処理
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
    # 出力
    print("correct")

if __name__ == '__main__':
    main()