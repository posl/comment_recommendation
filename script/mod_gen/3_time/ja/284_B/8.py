def main():
    # 1行目の入力
    T = int(input())
    # T個のテストケースについて処理を行う
    for i in range(T):
        # 2行目の入力
        N = int(input())
        # 3行目の入力
        A = list(map(int, input().split()))
        # Aの中に奇数が何個あるかをカウントする
        cnt = 0
        for j in range(N):
            if A[j] % 2 == 1:
                cnt += 1
        # 結果を出力する
        print(cnt)

if __name__ == '__main__':
    main()