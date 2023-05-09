def main():
    # 入力
    A, B = map(int, input().split())
    # 処理
    ans = 0
    if A == 0 and B == 0:
        ans = 0
    elif A == 0:
        ans = B - 1
    elif B == 0:
        ans = A - 1
    else:
        ans = A + B
    # 出力
    print(ans)

if __name__ == '__main__':
    main()