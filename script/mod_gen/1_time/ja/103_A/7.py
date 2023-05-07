def main():
    # 入力
    A = list(map(int, input().split()))
    # 処理
    ans = 0
    if A[0] > A[1]:
        ans += A[0] - A[1]
    if A[2] > A[1]:
        ans += A[2] - A[1]
    # 出力
    print(ans)

if __name__ == '__main__':
    main()