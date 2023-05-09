def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 逆順に見ていく
    A.reverse()
    # 1人目の出席番号を出力する
    print(A[0])
    # 2人目以降の出席番号を出力する
    for i in range(1, N):
        print(A[i] - sum(A[:i]))

if __name__ == '__main__':
    main()