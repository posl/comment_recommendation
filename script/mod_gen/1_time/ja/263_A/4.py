def main():
    # 入力
    A, B, C, D, E = map(int, input().split())
    # 処理
    if A == B == C and D == E:
        print("Yes")
    elif A == B and C == D == E:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()