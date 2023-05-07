def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    A.sort()
    # 出力
    print(A[1] - A[0])

if __name__ == '__main__':
    main()