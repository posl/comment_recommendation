def main():
    # 1行目の入力
    A, B, C = map(int, input().split())
    # 3つの整数が全て同じかどうか
    if A == B == C:
        print("No")
    # 3つの整数のうち、2つが同じかどうか
    elif A == B or A == C or B == C:
        print("Yes")
    # 3つの整数が全て異なる場合
    else:
        print("No")

if __name__ == '__main__':
    main()