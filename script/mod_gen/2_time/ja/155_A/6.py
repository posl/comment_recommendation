def main():
    # 入力
    A, B, C = map(int, input().split())
    # 処理
    if A == B or A == C or B == C:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()