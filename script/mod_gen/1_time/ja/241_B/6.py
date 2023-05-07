def main():
    # 1行目
    N, M = map(int, input().split())
    # 2行目
    A = list(map(int, input().split()))
    # 3行目
    B = list(map(int, input().split()))
    # Aの中にBの要素があるかどうかを判定する。
    # あればYes、なければNo
    if all([b in A for b in B]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()