def main():
    # 入力
    A, B = map(int, input().split())
    # 処理
    S_A = sum(map(int, list(str(A))))
    S_B = sum(map(int, list(str(B))))
    # 出力
    if S_A >= S_B:
        print(S_A)
    else:
        print(S_B)

if __name__ == '__main__':
    main()