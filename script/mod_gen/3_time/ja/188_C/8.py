def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #勝ち負けの情報を格納するリスト
    win = [0] * (2 ** N)
    #勝ち負けの情報を格納
    for i in range(N):
        for j in range(2 ** i):
            if A[2 * j] > A[2 * j + 1]:
                win[2 * j] = 1
            else:
                win[2 * j + 1] = 1
    #勝ち負けの情報をもとに、準優勝者の番号を出力
    for i in range(2 ** N):
        if win[i] == 0:
            print(i + 1)
            break

if __name__ == '__main__':
    main()